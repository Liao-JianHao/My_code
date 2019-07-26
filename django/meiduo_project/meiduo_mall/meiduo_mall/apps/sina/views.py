from django.shortcuts import render,redirect
from django.views import View
from django import http
from django.conf import settings
from django.contrib.auth import login
from django_redis import get_redis_connection
from django.conf import global_settings

from re import match
import logging
import json
from meiduo_mall.libs.captcha.captcha import captcha

from .models import OAuthSinaUser
from . import sinaweibopy3
from meiduo_mall.utils.response_code import RETCODE
from oauth.utils import DataSerializer
from users.models import User
from carts.utils import merge_carts


logger = logging.getLogger('django')

class SinaOAuthView(View):
    def get(self, request):
        client = sinaweibopy3.APIClient(app_key=settings.APP_KEY, app_secret=settings.APP_SECRET,
                                        redirect_uri=settings.REDIRECT_URL)

        login_url = client.get_authorize_url()

        return http.HttpResponseRedirect(login_url)


class SinaOAuthCallbackView1(View):
    """微博登录后回调处理"""

    def get(self, request):

        # 获取查询字符串中的code
        code = request.GET.get('code')

        client = sinaweibopy3.APIClient(app_key=settings.APP_KEY, app_secret=settings.APP_SECRET,
                                        redirect_uri=settings.REDIRECT_URL)
        try:
            result = client.request_access_token(code)
            access_token = result.access_token
        except Exception as e:
            logger.error(e)

            return http.JsonResponse({'code': RETCODE.SERVERERR, 'errmsg': '微博服务器不可用'})

        try:
            sina_user = OAuthSinaUser.objects.get(uid=result['uid'])
        except OAuthSinaUser.DoesNotExist:

            access_token = DataSerializer.generate_data_signature(access_token)
            return render(request, 'sina_callback.html', {'access_token': access_token})

        else:
            user = sina_user.user
            login(request, user)
            response = redirect('contents:index')
            response.set_cookie('username', user.username, max_age=settings.SESSION_COOKIE_AGE)
            return response



    def post(self, request):
        json_dict = json.loads(request.body.decode())
        print(json_dict)
        access_token = json_dict.get('access_token')
        password = json_dict.get('password')
        mobile = json_dict.get('mobile')
        sms_code = json_dict.get('sms_code')


        if not all([access_token, password, mobile]):
            return http.HttpResponseForbidden("缺少必传参数")
        if not match(r'^[\w]{8,20}$', password):
            return http.HttpResponseForbidden('请输入8-20位的密码')
        if not match(r'^1[3-9]\d{9}', mobile):
            return http.HttpResponseForbidden('请输入正确的手机号码')

        redis_conn = get_redis_connection('verify_code')
        sms_code_server = redis_conn.get('sms_%s' % mobile)
        if sms_code_server is None or sms_code_server.decode() != sms_code:
            return http.HttpResponseForbidden('短信验证码有误')

        openid = DataSerializer.check_data_signature(access_token)
        if openid is None:
            return http.HttpResponseForbidden('access_token已过期')

        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:  # 没有则创建，此时的用户名为手机号
            user = User.objects.create_user(username=mobile, mobile=mobile, password=password)
        else:  # 如果有则检查密码
            if user.check_password(password) is False:
                return http.HttpResponseForbidden('账号或密码错误')

        OAuthSinaUser.objects.create(user=user, uid=access_token)
        login(request, user)
        response = http.JsonResponse({'status': RETCODE.OK})  # 不能反解析，因为之前记录了从哪来
        response.set_cookie('username', user.username,
                            max_age=global_settings.SESSION_COOKIE_AGE)  # SESSION_COOKIE_AGE全局的cookie到期时间
        merge_carts(request, user, response)
        return response


