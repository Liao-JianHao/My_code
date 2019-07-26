
from rest_framework.generics import CreateAPIView,ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from meiduo_admin.serializers.users import AdminAuthorizeSerializer, UsersInfoSerializer
from users.models import User


# class AdminAuthorizeView(APIView):
#
#     def post(self, request):
#         serializer = AdminAuthorizeSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
class AdminAuthorizeView(CreateAPIView):

    serializer_class = AdminAuthorizeSerializer


class UserInfoView(ListCreateAPIView):
    """用户信息"""
    permission_classes = [IsAdminUser]  # 接口限制
    serializer_class = UsersInfoSerializer  # 序列化器类

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            users = User.objects.filter(username__contains=keyword, is_staff=False)
        else:
            users = User.objects.filter(is_staff=False)
        return users




