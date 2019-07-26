from rest_framework import serializers


from goods.models import SPUSpecification,GoodsCategory,GoodsChannel


class SPUSpecsSerializer(serializers.ModelSerializer):
    """SPU 规格"""
    # 序列关联嵌套
    spu = serializers.StringRelatedField(label='SPU')
    spu_id = serializers.IntegerField(label='SPU ID')

    # options = GoodsOptionSerializer(label='选项', many=True)
    class Meta:
        model = SPUSpecification
        exclude = ('create_time', 'update_time')


class SKUSCategoriesSerializer(serializers.ModelSerializer):
    """一级分类"""

    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')

class SbusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')

class SKUSCategories2Serializer(serializers.ModelSerializer):
    sbus = SbusSerializer(label='sbus', many=True)
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name','sbus')