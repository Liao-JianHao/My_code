from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import UpdateModelMixin
from rest_framework.decorators import action


from orders.models import OrderInfo
from meiduo_admin.serializers.orders import OrdersSerializer, OrderDetailSerializer, OrderStatusSerializer


class OrdersViewSite(UpdateModelMixin, ReadOnlyModelViewSet):
    """订单"""
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        """重写"""
        keyword = self.request.query_params.get('keyword')

        if keyword:
            orders = OrderInfo.objects.filter(skus__sku__name__contains=keyword)
        else:
            orders = OrderInfo.objects.all()
        return orders

    def get_serializer_class(self):
        """重写"""
        if self.action == 'list':
            return OrdersSerializer
        elif self.action == 'retrieve':
            return OrderDetailSerializer
        else:
            return OrderStatusSerializer

    @action(methods=['put'], detail=True)
    def status(self, request, pk):
        """自定义"""
        return self.update(request, pk)
