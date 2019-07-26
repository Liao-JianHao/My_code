from rest_framework import serializers
from django.utils import timezone
from rest_framework.exceptions import APIException
from django.db import transaction

import re

from users.models import User
from goods.models import SPU,GoodsVisitCount, GoodsChannel, GoodsCategory, GoodsChannelGroup,SKUImage,SKU,SKUSpecification,SPUSpecification,SpecificationOption

from meiduo_mall.utils.fastdfs.fast_storage import FastDFSStorage

class AdminAuthorizeSerializer(serializers.ModelSerializer):
    """用户认证"""
    token = serializers.CharField(label='JWT Token', read_only=True)
    username = serializers.CharField(label='用户名')

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'token']
        extra_kwargs = {
            'password':{
                'write_only': True,

            }
        }


    def validate(self, attrs):
        """attrs 参数是反序列化器data中传入"""
        username = attrs['username']
        password = attrs['password']

        try:
            # is_staff
            user = User.objects.get(username=username, is_staff=True)
        except User.DoesNotExist:
            raise serializers.ValidationError('用户不存在')
        else:
            if not user.check_password(password):
                raise serializers.ValidationError('密码错误')
        attrs['user'] = user
        return attrs


    def create(self, validated_data):
        """validated_data 是校验过后的数据"""
        user = validated_data['user']

        # 设置最新登录时间
        user.last_login = timezone.now()
        user.save()

        # 使用jwt
        # 服务器生成jwt token, 保存当前用户的身份信息
        from rest_framework_jwt.settings import api_settings

        # 生成payload载荷(比如飞机上承载的货物)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # 生成jwt token的方法
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        user.token = token

        return user


class GoodVisitSerializer(serializers.ModelSerializer):
    """商品访问序列化类"""
    category = serializers.StringRelatedField(label='分类名称')
    class Meta:
        model = GoodsVisitCount
        fields = ['category', 'count']


class UsersInfoSerializer(serializers.ModelSerializer):
    """用户信息"""
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email', 'password')
        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 20,
                'error_messages': {
                    'min_length': '用户名最小长度为5',
                    'max_length': '用户名最大长度为20'
                }
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '密码最小长度为8',
                    'max_length': '密码最大长度为20'
                }
            }
        }

    def validate_mobile(self, value):
        # 验证手机号
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号有误')
        # 验证手机号是否被注册
        count = User.objects.filter(mobile=value).count()
        if count > 0:
            raise serializers.ValidationError('手机号已注册')
        return value

    def create(self, validated_data):
        # 因为要加密敏感信息（密码）
        user = User.objects.create_user(**validated_data)
        return user


class ChannelsSerializer(serializers.ModelSerializer):
    """频道管理"""
    category = serializers.StringRelatedField(label='一级分类名称')
    group = serializers.StringRelatedField(label='频道组的名称')

    category_id = serializers.IntegerField(label='一级分类id')
    group_id = serializers.IntegerField(label='频道组id')
    class Meta:
        model = GoodsChannel
        fields = ('id', 'category', 'category_id', 'group', 'group_id', 'sequence', 'url')

    def validate_category_id(self, value):
        """一级分类是否存在"""
        try:
            GoodsCategory.objects.get(id=value, parent=None)
        except GoodsCategory.DoesNotExist:
            raise serializers.ValidationError('一级分类不存在')

        return value

    def validate_group_id(self, value):
        """频道组是否存在"""
        try:
            GoodsChannelGroup.objects.get(id=value)
        except GoodsChannelGroup.DoesNotExist:
            raise serializers.ValidationError('频道组不存在')

        return value


class ChannelTypeSerializer(serializers.ModelSerializer):
    """频道类型"""
    class Meta:
        model = GoodsChannelGroup
        fields = ('id', 'name')


class ChannelCategorySerializer(serializers.ModelSerializer):
    """一级分类"""
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):
    """图片管理"""
    sku_id = serializers.IntegerField(label='SKU_ID')
    sku = serializers.StringRelatedField(label='SKU商品')
    class Meta:
        model = SKUImage
        exclude = ('create_time', 'update_time')

    def validate_sku_id(self, value):
        try:
            sku = SKU.objects.get(id=value)
        except SKU.DoesNotExists:
            raise serializers.ValidationError('SKU商品不存在')
        return sku

    def update(self, instance, validated_data):

        file = validated_data['image']
        sku = validated_data['sku_id']


        fdfs = FastDFSStorage()
        try:
            file_id = fdfs.save(file.name, file)
        except Exception:
            raise APIException('上传文件失败')

        # 修改SKU图片数据
        instance.sku = sku
        instance.image = file_id
        instance.save()

        return instance

    # ModelSerializer->create->SKUImage.objects.create()
    def create(self, validated_data):

        file = validated_data['image']
        sku = validated_data['sku_id']


        fdfs = FastDFSStorage()
        try:
            file_id = fdfs.save(file.name, file)
        except Exception:
            raise APIException('上传文件失败')

        # 保存上传图片记录
        sku_image = SKUImage.objects.create(
            sku=sku,
            # sku_id=sku.id,
            image=file_id
        )

        # sku商品的默认图片设置
        if not sku.default_image:
            sku.default_image = sku_image.image.url
            sku.save()

        return sku_image


class ImageSKUSerializer(serializers.ModelSerializer):
    """SKU的图片序列化器"""

    class Meta:
        model = SKU
        fields = ('id', 'name')


class SKUSpecsSerializer(serializers.ModelSerializer):
    """SKU的规格"""
    spec_id = serializers.IntegerField(label='规格id')
    option_id = serializers.IntegerField(label='选项id')
    class Meta:
        model = SKUSpecification
        fields = ('spec_id', 'option_id')


class SKUSerializer(serializers.ModelSerializer):
    """SKU序列化器累"""
    spu_id = serializers.IntegerField(label='SPU_ID')
    spu = serializers.StringRelatedField(label='SPU名称')

    category_id = serializers.IntegerField(label='种类_ID')
    category = serializers.StringRelatedField(label='种类')

    specs = SKUSpecsSerializer(label='规格', many=True)
    class Meta:
        model = SKU
        exclude = ('default_image', 'create_time', 'update_time')


    def validate(self, attrs):
        category_id = attrs['category_id']

        try:
            spu_catgory = GoodsCategory.objects.get(id=category_id, parent=None)
        except GoodsCategory.DoesNotExist:
            raise serializers.ValidationError('第三级分类不存在')

        spu_id = attrs['spu_id']

        try:
            spu = SPU.objects.get(id=spu_id)
        except SPU.DoesNotExist:
            raise serializers.ValidationError('SPU不存在')

        # 检查分类是否一致
        if category_id != spu.category1_id:
            raise serializers.ValidationError('第三级分类数据有误')

        spu_specs = spu.specs.all()  # 获取和spu关联的规格数据
        spu_specs_count = spu_specs.count()

        specs = attrs['specs']
        if spu_specs_count != len(specs):
            raise serializers.ValidationError('SKU规格数据不完整')

        spu_specs_ids = [spec.id for spec in spu_specs]
        specs_ids = [spec.get('spec_id') for spec in specs]

        if spu_specs_ids.sort() != specs_ids.sort():
            raise serializers.ValidationError('SKU规格数据有误')

        for spec in specs:
            spec_id = spec.get('spec_id')
            option_id = spec.get('option_id')

            options = SpecificationOption.objects.filter(spec_id=spec_id)
            options_ids = [option.id for option in options]

            if option_id not in options_ids:
                raise serializers.ValidationError('规格选项数据有误')

        return attrs



    def create(self, validated_data):
        """创建模型对象时，是写入两张表，所以要重写create方法"""
        specs = validated_data.pop('specs')

        # 不用创建保存点，因为没有逻辑代码
        with transaction.atomic():

            # sku = super(SKUSerializer, self).create(validated_data)
            #
            #
            # for spec in specs:
            #
            #     SPUSpecification.objects.create(
            #         sku=sku,
            #         # spec_id=spec.get('spec_id'),
            #         # option_id=spec.get('option_id')
            #
            #         spec_id = spec.get('spec_id'),
            #         option_id = spec.get('option_id')
            #     )

            sku = super().create(validated_data)

            # 添加sku商品规格选项数据
            for spec in specs:
                # 获取spec_id和option_id
                spec_id = spec.get('spec_id')
                option_id = spec.get('option_id')

                SKUSpecification.objects.create(
                    sku=sku,
                    spec_id=spec_id,
                    option_id=option_id
                )

        return sku



class SPUSimpleSerializer(serializers.ModelSerializer):
    """SPU序列化器类"""
    class Meta:
        model = SPU
        fields = ('id', 'name')


class SKUSCategoriesSerializer(serializers.ModelSerializer):
    """SKU 商品分类"""
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')



class GoodsOptionSerializer(serializers.ModelSerializer):
    """规格选项"""
    class Meta:
        model = SpecificationOption
        fields = ('id', 'value')

