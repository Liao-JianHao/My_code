from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from meiduo_admin.serializers.spu import SPUSpecsSerializer,SKUSCategoriesSerializer,SKUSCategories2Serializer
from goods.models import SPUSpecification,GoodsCategory,GoodsChannel


class GoodsSpecsView(ReadOnlyModelViewSet):
    """SPU 选项"""
    permission_classes = [IsAdminUser]
    pagination_class = None
    serializer_class = SPUSpecsSerializer

    # def get_object(self):
    #     # 获取pk
    #     pk = self.kwargs['pk']
    #     spu = SPUSpecification.objects.filter(pk=pk)
    #     serializer = SKUSCategoriesSerializer(spu, many=True)
    #     return Response(serializer.data)

class SPUCategoriesView(ListAPIView):
    pagination_class = None
    permission_classes = [IsAdminUser]
    serializer_class = SKUSCategoriesSerializer
    queryset = GoodsCategory.objects.filter(parent=None)


class SPUCategories1View(RetrieveAPIView):
    pagination_class = None
    permission_classes = [IsAdminUser]
    serializer_class = SKUSCategories2Serializer

    def get_object(self):
        pk = self.kwargs['keyword']
        queryset = GoodsCategory.objects.filter(name=pk)
        return queryset
