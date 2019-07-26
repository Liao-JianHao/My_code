from django.conf.urls import url
from . import views

urlpatterns = [
    url('^oauth/weibo/login/', views.SinaOAuthView.as_view()),  # 微博授权页面
    url('^oauth/sina/user/$', views.SinaOAuthCallbackView1.as_view()),  # 微博回调页面
    # url('^oauth/weibo/login/', views.OauthWBURLView.as_view()),  # 微博授权页面
    # url('^oauth/sina/user/(?P<code>\w+)', views.OauthWBUserView.as_view()),  #

]

