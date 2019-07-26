from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView

from meiduo_admin.serializers.users import ChannelsSerializer,ChannelTypeSerializer,ChannelCategorySerializer
from goods.models import GoodsChannel,GoodsChannelGroup,GoodsCategory

class ChannelsView(ModelViewSet):
    """频道管理界面"""
    permission_classes = [IsAdminUser]
    serializer_class = ChannelsSerializer
    queryset = GoodsChannel.objects.all()


class ChannelTypeView(ListAPIView):
    """频道类型"""
    permission_classes = [IsAdminUser]
    serializer_class = ChannelTypeSerializer
    queryset = GoodsChannelGroup.objects.all()
    pagination_class = None

class ChannelCategoryView(ListAPIView):
    """一级分类"""
    permission_classes = [IsAdminUser]
    serializer_class = ChannelCategorySerializer
    queryset = GoodsCategory.objects.filter(parent=None)

    # 注：关闭分页
    pagination_class = None