from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from users.models import User
from meiduo_admin.serializers.permission_user_manage import PermissionSerializer,ContentTypeSerializer,GroupSerializer,UserManageSerializer


class PermissionViewSet(ModelViewSet):
    """权限管理类"""
    permission_classes = [IsAdminUser]
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()

    def content_type(self, request):
        content_type = ContentType.objects.all()
        serializer = ContentTypeSerializer(content_type, many=True)
        return Response(serializer.data)


class GroupViewSet(ModelViewSet):
    """组管理类"""
    permission_classes = [IsAdminUser]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def simple(self, request):
        permission = Permission.objects.all()
        serializer = PermissionSerializer(permission, many=True)
        return Response(serializer.data)


class UserManageViewSet(ModelViewSet):
    """管理员类"""
    permission_classes = [IsAdminUser]
    serializer_class = UserManageSerializer
    queryset = User.objects.filter(is_staff=True)

    def admins(self, request):
        admins = Group.objects.all()
        serializer = GroupSerializer(admins, many=True)
        return Response(serializer.data)