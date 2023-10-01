# Rest
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated, AllowAny
# Django
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Apps Producto
from applications.producto.models import Product
# Apps Venta
from .models import Sale, SaleDetail
from .serializers import (
    ProcesoVendaSerialaizer2,
    VentaReporteSerializer 
)


class VentasViewSet(viewsets.ViewSet):
    
    authentication_classes = (TokenAuthentication,)   
    queryset = Sale.objects.all()
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]    


    def list(self, request, *args, **kwargs):
        queryset = Sale.objects.all()
        
        serializer = VentaReporteSerializer(queryset, many=True)
        return Response(serializer.data)

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
        

    def retrieve(self, request, pk=None):
        venta = get_object_or_404(Sale.objects.all(), pk=pk)
        serializer = VentaReporteSerializer(venta)
        
        return Response(serializer.data)


    def partial_update(self, request, pk=None):
        venta = Sale.objects.get(id=pk)
        serializer = VentaReporteSerializer(venta)
        
        return Response(serializer.data)
        

    def destroy(self, request, pk=None):
        print ("*************")
        
        return Response({"probando":"viwsets5"})     