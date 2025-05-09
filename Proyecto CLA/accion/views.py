from django.shortcuts import render
from .models import Interfaz
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

def crud(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/crud.html', context)

def gracias(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/gracias.html', context)
