from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from django.db.models import Q

from goods.models import SKUImage, SKU,SPU
from meiduo_admin.serializers.users import ImageSerializer,ImageSKUSerializer,SKUSerializer,SPUSimpleSerializer

class ImageViewSet(ModelViewSet):
    """图片界面"""
    permission_classes = [IsAdminUser]
    serializer_class = ImageSerializer
    queryset = SKUImage.objects.all()


class ImageSKUView(ListAPIView):
    """SKU 图片下拉栏"""
    permission_classes = [IsAdminUser]
    pagination_class = None
    serializer_class = ImageSKUSerializer
    queryset = SKU.objects.all()


class SKUViewSite(ModelViewSet):
    """SKU界面"""
    permission_classes = [IsAdminUser]
    serializer_class = SKUSerializer
    def get_queryset(self):
        # keyword = self.request.query_params.get('keyword')
        #
        # if keyword:
        #     skus = SKU.objects.filter(Q(name__contains=keyword)|Q(caption__contains=keyword))
        # else:
        #     skus = SKU.objects.all()
        #
        # return skus

        keyword = self.request.query_params.get('keyword')

        if keyword:
            # |
            skus = SKU.objects.filter(Q(name__contains=keyword) |
                                      Q(caption__contains=keyword))
        else:
            skus = SKU.objects.all()

        return skus


class SPUView(ListAPIView):
    """SKU中的SPU下拉栏"""
    permission_classes = [IsAdminUser]
    serializer_class = SPUSimpleSerializer
    queryset = SPU.objects.all()
    pagination_class = None