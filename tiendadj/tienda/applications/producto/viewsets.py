# Rest
from rest_framework import viewsets
from rest_framework.response import Response
# Apps Products
from .models import Colors, Product
from .serializers import (
    ColorsSerializer, 
    ProductSerializer,
    ProductSerializer2,
    PaginationSerializer,
)


class ColorViewSet(viewsets.ModelViewSet):
    
    serializer_class = ColorsSerializer
    queryset = Colors.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProductSerializer2
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer
    

    def perform_create (self, serializer):
        serializer.save(
            video = 'https://www.youtube.com/'
        )
        
    def list(self, request, *args, **kwargs):
        queryset = Product.objects.prodoctos_por_user(self.request.user)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

