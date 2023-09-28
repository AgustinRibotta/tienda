from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/product/por-usuario/',
        views.ListProductUser.as_view(),
        name='producto-user'
    ),
    path(
        'api/product/stok/',
        views.ListProductStokUser.as_view(),
        name='producto-stok'
    ),
    path(
        'api/product/genero/<gender>/',
        views.ListProducGenero.as_view(),
        name='producto-genero'
    ),
    path(
        'api/product/filtrar/',
        views.FiltraProduictos.as_view(),
        name='producto-filtrar'
    ),
]
