# Rest
from rest_framework.routers import DefaultRouter
# Apps Producto
from . import viewsets

router = DefaultRouter()

router.register(r'ventas', viewsets.VentasViewSet, basename="ventas")


urlpatterns = router.urls