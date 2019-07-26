from rest_framework import serializers

from goods.models import SPUSpecification,SpecificationOption


class SpecsSerializer(serializers.ModelSerializer):
    """规格页面序列化"""
    spu = serializers.StringRelatedField(label='SPU名称')
    spu_id = serializers.IntegerField(label='SPU_ID')
    class Meta:
        model = SPUSpecification
        fields = ('id', 'name', 'spu', 'spu_id')


class SpecsSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPUSpecification
        fields = ('id', 'name')

class SpecsOptionSerializer(serializers.ModelSerializer):
    """规格选项页面序列化"""
    spec_id = serializers.IntegerField(label='规格选项ID')
    spec = serializers.StringRelatedField(label='规格名称')
    class Meta:
        model = SpecificationOption
        fields = ('id', 'value', 'spec_id', 'spec')
