# Django
from django.utils import timezone
from django.shortcuts import render
# Rest
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
# Ventas 
from .models import  Sale, SaleDetail
from .serializers import (
    VentaReporteSerializer,
    ProcesoVendaSerialaizer,
    ProcesoVendaSerialaizer2    
)
# Productos
from applications.producto.models import Product


# Listado de reporte de ventas
class ReporteVentasList(ListAPIView):
    
    serializer_class = VentaReporteSerializer
    
    def get_queryset(self):
        
        return Sale.objects.all()


#  Genearacion de nueva venta
class RegistroVenta(CreateAPIView):
    
    authentication_classes = (TokenAuthentication,)   
    permission_classes = [IsAuthenticated]
    
    serializer_class = ProcesoVendaSerialaizer
    
    # De esta manera recuperamos los datos de un serializador que no depende de un modelo
    def create(self, request, *args, **kwargs):
        serializer = ProcesoVendaSerialaizer(data=request.data)
        # Si lo que vino no es correcto madna un error
        serializer.is_valid(raise_exception=True)
        # De esta manera lo recuperamos solo si se cumple el anterior paso 
        venta = Sale.objects.create(
            date_sale = timezone.now(),
            amount = 0,
            count =0,
            type_invoce = serializer.validated_data['type_invoce'], 
            type_payment =serializer.validated_data['type_payment'],
            adreese_send =serializer.validated_data['adreese_send'], 
            user = self.request.user
        )
        # vartiables para venta 
        amount = 0
        count = 0 
        # Recuperamos productos de venta
        productos = serializer.validated_data['productos']
        #
        ventas_detail = []
        #
        for producto in productos:
            prod = Product.objects.get(id=producto['pk'])
            venta_detalle = SaleDetail(
                sale = venta,
                product = prod,
                count = producto['count'],
                price_purchase = prod.price_purchase,
                price_sale = prod.price_sale,  
            )
            #
            amount = amount + prod.price_sale*producto['count']
            count = count + producto['count']
            # Ventas
            ventas_detail.append(venta_detalle)
            
        venta.amount = amount
        venta.count = count
        venta.save()
        
        SaleDetail.objects.bulk_create(ventas_detail)
        
        return Response(
            
            {
                'msj':'Venta exitosa'
            }
        
        )
        
        
#  Genearacion de nueva venta (Reciviendo un array con los productos)
class RegistroVenta2(CreateAPIView):
    
    authentication_classes = (TokenAuthentication,)   
    permission_classes = [IsAuthenticated]
    
    serializer_class = ProcesoVendaSerialaizer2
    
    # De esta manera recuperamos los datos de un serializador que no depende de un modelo
    def create(self, request, *args, **kwargs):
        serializer = ProcesoVendaSerialaizer2(data=request.data)
        # Si lo que vino no es correcto madna un error
        serializer.is_valid(raise_exception=True)
        # De esta manera lo recuperamos solo si se cumple el anterior paso 
        venta = Sale.objects.create(
            date_sale = timezone.now(),
            amount = 0,
            count =0,
            type_invoce = serializer.validated_data['type_invoce'], 
            type_payment =serializer.validated_data['type_payment'],
            adreese_send =serializer.validated_data['adreese_send'], 
            user = self.request.user
        )
        # vartiables para venta 
        amount = 0
        count = 0 
        # Recuperamos productos de venta
        productos = Product.objects.filter(
            id__in = serializer.validated_data['productos']
        )
        #
        cantidades =  serializer.validated_data['cantidades']
        #
        ventas_detail = []
        # De esta manera iteramos en los productos y la cantidad de los mimsos
        for producto, cantidad in zip(productos, cantidades):
            venta_detalle = SaleDetail(
                sale = venta,
                product = producto,
                count = cantidad,
                price_purchase = producto.price_purchase,
                price_sale = producto.price_sale,  
            )
            #
            amount = amount + producto.price_sale*cantidad
            count = count + cantidad
            # Ventas
            ventas_detail.append(venta_detalle)
            
        venta.amount = amount
        venta.count = count
        venta.save()
        
        SaleDetail.objects.bulk_create(ventas_detail)
        
        return Response(
            
            {
                'msj':'Venta exitosa'
            }
        
        )
        