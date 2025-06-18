from django.contrib import admin
from django.urls import path, include
from . import views

from .views import configuracion_admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.layout, name="layout"),
    path('layout/', views.layout, name='layout'),
    path('home.html', views.home, name="home"),
    path('quienesSomos.html', views.quienesSomos, name='quienesSomos'),
    path('novedades.html', views.novedades, name='novedades'),
    path('contacto.html', views.contacto, name='contacto'),
    path('inicioSesion.html', views.inicioSesion, name='inicioSesion'),
    path('usuarios/registro/', views.registro, name='registro'),
    path('carrito.html', views.carrito_view, name='carrito'),
    path('configuracion.html', views.configuracion, name='configuracion'),
    path('configuracion/', configuracion_admin, name='configuracion'),
    path('proveedores/', views.proveedores_list, name='proveedores_list'),
    path('proveedor/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('analiticas/', views.analiticas, name='analiticas'),
    path('gestionUsuario/', views.gestionUsuario, name='gestionUsuario'),
    path('loginadmin.html', views.loginadmin, name='loginadmin'),
]