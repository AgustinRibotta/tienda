#
from rest_framework import serializers, pagination
#
from .models import Product, Colors


# Color
class ColorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Colors
        fields = [
            'color'
        ]


# Product
class ProductSerializer(serializers.ModelSerializer):
    
    token_id = serializers.CharField(default=True)
    colors = ColorsSerializer(many = True)
    
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'man',
            'woman',
            'weight',
            'price_purchase',
            'price_sale',
            'main_image',
            'image1',
            'image2',
            'image3',
            'image4',
            'colors',
            'video',
            'stok',
            'num_sales',
            'user_created',
            'token_id',
        ]

  
# Paginacion
class PaginationSerializer(pagination.PageNumberPagination):
    
    page_size = 5
    max_page_size = 50
    
    
# Product
class ProductSerializer2(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('__all__')
    

