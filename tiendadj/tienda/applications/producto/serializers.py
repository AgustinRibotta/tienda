from rest_framework import serializers
#
from .models import Product 


# Product
class ProductSerializer(serializers.ModelSerializer):
    
    token_id = serializers.CharField(default=True)
    
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
    