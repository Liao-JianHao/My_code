from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,ListAPIView,ListCreateAPIView

from meiduo_admin.serializers.goods import GoodsSerializer,BrandSerializer,GoodsCategorySerializer,SPUSerializer
from goods.models import SPU,Brand,GoodsCategory,GoodsChannel


class GoodsViewSite(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = GoodsSerializer
    queryset = SPU.objects.all()

    def brands(self, request):
        """品牌"""
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    # def categories1(self, request):
    #     """种类"""
    #     categories = GoodsCategory.objects.filter(parent=None)
    #     serializer = GoodsCategorySerializer(categories, many=True)
    #     return Response(serializer.data)
    #
    # def categories2(self, request, pk):
    #     """种类"""
    #     subs = GoodsCategory.objects.filter(parent=pk)
    #     serializer = GoodsCategorySerializer(subs, many=True)
    #     return Response(serializer.data)


class SUPAPIView(ListCreateAPIView):
    pagination_class = None
    serializer_class = SPUSerializer
    queryset = SPU.objects.all()

