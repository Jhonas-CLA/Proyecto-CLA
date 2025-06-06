from .models import Interfaz
from django.shortcuts import render, redirect
from django.contrib.auth import login

# Create your views here.

def layout(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/layout.html', context)


def home(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/home.html', context)

def quienesSomos(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/quienesSomos.html', context)

def novedades(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/novedades.html', context)

def contacto(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/contacto.html', context)

def inicioSesion(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/inicioSesion.html', context)

def novedades1(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/novedades1.html', context)

def registro(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/registro.html', context)

def gracias(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/gracias.html', context)

def carrito_view(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/gracias.html', context)


