from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.layout, name="layout"),
    path('home.html', views.home,name="home"),
    path('quienesSomos.html', views.quienesSomos,name= "quienesSomos"),
    path('novedades.html', views.novedades, name= "novedades"),
    path('contacto.html', views.contacto, name= "contacto"),
    path('inicioSesion.html', views.inicioSesion, name= "inicioSesion"),
    path('novedades1.html', views.novedades1, name="novedades1"),
    path('registro.html', views.registro, name= "registro"),
    path('crud.html', views.crud, name= "crud"),
    path('gracias.html', views.gracias, name="gracias")

]