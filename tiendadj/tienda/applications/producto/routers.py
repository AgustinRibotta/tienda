# Rest
from rest_framework.routers import DefaultRouter
# Apps Producto
from . import viewsets

router = DefaultRouter()

router.register(r'colors', viewsets.ColorViewSet, basename="colors")
router.register(r'productos', viewsets.ProductViewSet, basename="productos")

urlpatterns = router.urls