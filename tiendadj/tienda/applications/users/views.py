# Rest
from rest_framework.views import APIView
# 
from firebase_admin import auth
# Dejango
from django.shortcuts import render
from django.views.generic import TemplateView
# Serialaizer
from .serializers import LoginSocialSerializer
# Models
from .models import User


class LoginUser(TemplateView):
    template_name = "users/login.html"


# Regstro de googler
class GooglerLoginView(APIView):
    
    serializer_class = LoginSocialSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Recuperamos el token
        token = serializer.data.get('token_id')
        # Lo decodificamos
        decode_token = auth.verify_id_token(token)
        # Recuperamos los datos solicitaods
        email = decode_token['email']
        name = decode_token['name']
        avatar = decode_token['picture']
        verified = decode_token['email_verified']
        # Creamos nuestro User
        usuario, created = User.objects.get_or_create(
            email = email,
            defaults={
                'full_name' : name,
                'email' : email,
                'is_active' : True,
            }
        )
        # 
        return usuario, created