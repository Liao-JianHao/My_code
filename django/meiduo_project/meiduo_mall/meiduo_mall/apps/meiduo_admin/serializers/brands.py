from rest_framework import serializers
from rest_framework.exceptions import APIException

from meiduo_mall.utils.fastdfs.fast_storage import FastDFSStorage
from goods.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """品牌页面"""
    class Meta:
        model = Brand
        exclude = ('create_time', 'update_time')

    # def validate(self, attrs):


    def update(self, instance, validated_data):
        file = validated_data['logo']
        brand = validated_data['name']

        fdfs = FastDFSStorage()
        try:
            file_id = fdfs.save(file.name, file)
        except Exception:
            raise APIException('上传文件失败')

        instance.brand = brand
        instance.logo = file_id
        instance.save()

        return instance

    def create(self, validated_data):
        file = validated_data['logo']
        brand = validated_data['name']

        fdfs = FastDFSStorage()
        try:
            file_id = fdfs.save(file.name, file)
        except Exception:
            raise APIException('上传文件失败')

        brand_image = Brand.objects.create(name=brand, logo=file_id)

        if not brand.logo:
            brand.logo = brand_image.loge.url
            brand.save()

        return brand_image