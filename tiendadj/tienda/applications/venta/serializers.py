# Rest
from rest_framework import serializers
# Venta Model
from .models import Sale, SaleDetail

# Reporte de venta
class VentaReporteSerializer(serializers.ModelSerializer):
    
    productos = serializers.SerializerMethodField()
    
    class Meta:
        model = Sale 
        fields = (
        'id',
        'date_sale',
        'amount',
        'count',
        'type_invoce',
        'cancelado',
        'state',
        'adreese_send',
        'user',
        'productos',
    )
        
    def get_productos(self, obj):
        query = SaleDetail.objects.productos_por_ventas(obj.id)
        productos_serializados = DetailVentaSerilizer(query, many=True).data
        return productos_serializados
    

# Detail de venta
class DetailVentaSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = SaleDetail
        fields = (
        'id',
        'sale',
        'product',
        'count',
        'price_purchase',
        'price_sale',
        'anulate',
    )
        

# Proceso de ventda
class ProdcutVentaSerializer(serializers.Serializer):
    
    pk = serializers.IntegerField()
    count = serializers.IntegerField()

    # Serializador para solicitar un array
class ArrayIntegerSerializer(serializers.ListField):
    
    child = serializers.IntegerField()


class ProcesoVendaSerialaizer(serializers.Serializer):
    
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    productos = ProdcutVentaSerializer(many=True)
    

class ProcesoVendaSerialaizer2(serializers.Serializer):
    
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    # Serializador de tipo array
    productos = ArrayIntegerSerializer()
    cantidades = ArrayIntegerSerializer()
    
