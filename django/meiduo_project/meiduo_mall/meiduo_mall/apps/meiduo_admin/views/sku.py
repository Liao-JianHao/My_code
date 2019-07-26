from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from meiduo_admin.serializers.users import SKUSCategoriesSerializer
from goods.models import GoodsCategory

class SKUSCategoriesView(ListAPIView):
    """SKU分类"""
    permission_classes = [IsAdminUser]
    serializer_class = SKUSCategoriesSerializer
    queryset = GoodsCategory.objects.all()
    pagination_class = None

