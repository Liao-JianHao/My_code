from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from goods.models import Brand
from meiduo_admin.serializers.brands import BrandSerializer


class BrandViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()