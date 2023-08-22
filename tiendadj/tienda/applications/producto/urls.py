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
]
