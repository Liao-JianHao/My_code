from rest_framework import serializers
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from users.models import User


class PermissionSerializer(serializers.ModelSerializer):
    """权限管理序列化器类"""
    class Meta:
        model = Permission
        fields = '__all__'
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'name': {
                'read_only': True
            },
        }


class ContentTypeSerializer(serializers.ModelSerializer):
    """权限类型序列化器类"""
    class Meta:
        model = ContentType
        fields = ('id', 'name')

# class PermissionSimpleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Permission
#         fields = ('id', 'name')

class GroupSerializer(serializers.ModelSerializer):
    """组管理序列化器类"""
    class Meta:
        model = Group
        fields = '__all__'
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'name': {
                'read_only': True
            },
        }


class UserManageSerializer(serializers.ModelSerializer):
    """管理员序列化器类"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'mobile', 'password', 'user_permissions', 'groups')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': False,
                'allow_blank': True
            }
        }

    def create(self, validated_data):
        """创建管理员用户"""
        # 设置管理员标记is_staff为True
        validated_data['is_staff'] = True

        # 创建新的管理员用户
        user = super().create(validated_data)

        # 密码加密保存
        password = validated_data['password']

        if not password:
            # 管理员默认密码
            password = '123abc'

        user.set_password(password)
        user.save()

        return user

