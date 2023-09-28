#
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
#
from django.shortcuts import render
#
from .models import Product
# 
from .serializers import ProductSerializer


# 
class ListProductUser(ListAPIView):
    
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)   
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # recuperamos el user
        user = self.request.user
        return Product.objects.prodoctos_por_user(user)


#
class ListProductStokUser(ListAPIView):
    
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)   
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.prodoctos_con_stok()
    

#
class ListProducGenero(ListAPIView):
    
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        genero = self.kwargs['gender']
        return Product.objects.prodoctos_genero('genero')
    
    
#
class FiltraProduictos(ListAPIView):
    
    serializer_class = ProductSerializer

    def get_queryset(self):
        
        varon = self.request.query_params.get('man', None)
        mujer = self.request.query_params.get('woman', None)
        nombre = self.request.query_params.get('name', None)

        return Product.objects.filtrar_productos(
            man = varon,
            woman = mujer,
            name = nombre,
            )