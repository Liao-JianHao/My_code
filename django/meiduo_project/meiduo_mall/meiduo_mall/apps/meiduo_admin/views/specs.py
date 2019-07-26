from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from goods.models import SPUSpecification,SpecificationOption
from meiduo_admin.serializers.specs import SpecsSerializer,SpecsOptionSerializer,SpecsSimpleSerializer


class SpecsViewSet(ModelViewSet):
    """规格"""
    permission_classes = [IsAdminUser]
    serializer_class = SpecsSerializer
    queryset = SPUSpecification.objects.all()



class SpecsOptionViewSet(ModelViewSet):
    """规格选项"""
    permission_classes = [IsAdminUser]
    serializer_class = SpecsOptionSerializer
    queryset = SpecificationOption.objects.all()

    def simple(self, request):
        specs = SPUSpecification.objects.all()
        serializer = SpecsSimpleSerializer(specs, many=True)
        return Response(serializer.data)