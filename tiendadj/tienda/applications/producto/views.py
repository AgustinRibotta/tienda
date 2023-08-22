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
        # recuperamos el user
        user = self.request.user
        return Product.objects.prodoctos_con_stok()