from rest_framework import serializers

from orders.models import OrderInfo, OrderGoods
from goods.models import SKU

class OrdersSerializer(serializers.ModelSerializer):
    """订单序列化器"""
    create_time = serializers.DateTimeField(label='创建时间', format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = OrderInfo
        fields = ('order_id', 'create_time')



class OrderSKUSerializer(serializers.ModelSerializer):
    """订单SKU"""
    class Meta:
        model = SKU
        fields = ('default_image', 'name')

class OrderGoodsSerializer(serializers.ModelSerializer):
    """订单商品"""
    sku = OrderSKUSerializer(label='SKU')
    class Meta:
        model = OrderGoods
        fields = ('sku', 'price', 'count')

class OrderDetailSerializer(serializers.ModelSerializer):
    """订单详情"""
    # 序列嵌套化，需要将商品的图片等信息传入
    skus = OrderGoodsSerializer(label='订单商品', many=True)
    create_time = serializers.DateTimeField(label='创建时间', format='%Y-%m-%d %H-%M-%S')

    class Meta:
        model = OrderInfo
        exclude = ('address', 'update_time')



class OrderStatusSerializer(serializers.ModelSerializer):
    """修改订单状态"""
    class Meta:
        model = OrderInfo
        fields = ('order_id', 'status')
        read_only_fields = ('order_id',)

    def validate_status(self, attrs):
        if attrs not in [_ for _ in range(1, 7)]:
            return serializers.ValidationError('订单状态有误')
        return attrs