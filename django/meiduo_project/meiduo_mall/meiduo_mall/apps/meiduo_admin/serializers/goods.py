from rest_framework import serializers

from goods.models import SPU, Brand,GoodsCategory,GoodsChannel

class BrandSerializer(serializers.ModelSerializer):
    """品牌"""
    class Meta:
        model = Brand
        fields = ('id', 'name')




class GoodsCategorySerializer(serializers.ModelSerializer):
    """商品分类"""
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')







class GoodsSerializer(serializers.ModelSerializer):
    """SPU"""
    name = serializers.CharField(label='SPU名称')
    brand = serializers.StringRelatedField(label='品牌名称')
    brand_id = serializers.IntegerField(label='品牌id')
    category1_id = serializers.IntegerField(label='一级分类')
    category2_id = serializers.IntegerField(label='二级分类')
    category3_id = serializers.IntegerField(label='三级分类')

    class Meta:
        model = SPU

        exclude = ('create_time', 'update_time')



class SPUSerializer(serializers.ModelSerializer):
    """SPU"""
    name = serializers.CharField(label='SPU名称')
    brand = serializers.StringRelatedField(label='品牌名称')
    brand_id = serializers.IntegerField(label='品牌id')
    category1_id = serializers.IntegerField(label='一级分类')
    category2_id = serializers.IntegerField(label='二级分类')
    category3_id = serializers.IntegerField(label='三级分类')

    category1 = serializers.StringRelatedField(label='一级分类', read_only=True)
    category2 = serializers.StringRelatedField(label='二级分类', read_only=True)
    category3 = serializers.StringRelatedField(label='三级分类', read_only=True)

    class Meta:
        model = SPU

        exclude = ('create_time', 'update_time')


