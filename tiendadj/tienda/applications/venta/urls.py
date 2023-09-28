from django.urls import path, re_path
# Venta
from . import views

app_name = 'venta_app'

urlpatterns = [
    path(
        'api/venta/repote/',
        views.ReporteVentasList.as_view(),
        name='venta-reporte'
    ),
    path(
        'api/venta/create/',
        views.RegistroVenta.as_view(),
        name='venta-create'
    ),

]
