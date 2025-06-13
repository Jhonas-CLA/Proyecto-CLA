from django.contrib import admin
from django.urls import path, include
from . import views

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
    path('gracias.html', views.gracias, name="gracias"),
    path('carrito.html', views.carrito_view, name='carrito'),
    path('dashboard.html', views.dashboard, name= 'dashboard'),
    path('configuracion.html', views.configuracion, name='configuracion'),    
    path('configuracion/', views.configuracion_admin, name='configuracion'),
    path('guardar-configuracion/', views.guardar_configuracion, name='guardar_configuracion'),
]
