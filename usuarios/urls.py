from django.urls import path
from . import views
from .views import registro_view
from .views import login_view

urlpatterns = [
    path('logout/', views.cerrar_sesion, name='logout'),
    path('registro/', registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
]
