from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.carrito_view, name='carrito'),
]

from django.urls import path
from .views import listar_productos, agregar_producto, editar_producto, eliminar_producto, carrito_view

urlpatterns = [
    path('', listar_productos, name='listar_productos'),
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('editar/<int:pk>/', editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    path('carrito/', carrito_view, name='carrito'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)