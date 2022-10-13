from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

# Product View
class ProductViewSet(viewsets.ModelViewSet):
    # Operations to be performed
    queryset = Product.objects.all().order_by('id')
    # Class responsible for serializing the data
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def set_featured(self, request, pk):
        item = self.get_object()
        serializer = ProductSerializer(data=request.data)
        item.set_featured(1)
        item.save()
        return Response({'status': 'status changed'})