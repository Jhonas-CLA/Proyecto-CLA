from .models import Interfaz
from .models import Producto 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login

from .models import Administrador
from .forms import AdministradorForm

from .models import Proveedor
from .forms import ProveedorForm
# Create your views here.

def home(request):
    # Obtener los 10 productos más recientes o todos si hay menos de 10
    productos = Producto.objects.all()[:10]
    
    # Agrupar productos de 4 en 4 para cada slide del carrusel
    slides = []
    for i in range(0, len(productos), 4):
        slide_productos = productos[i:i+4]
        slides.append(slide_productos)
    
    context = {
        'slides': slides,
        'productos': productos
    }
    return render(request, 'accion/home.html', context)

def layout(request):
    # Misma lógica para layout.html
    productos = Producto.objects.all()[:10]
    
    slides = []
    for i in range(0, len(productos), 4):
        slide_productos = productos[i:i+4]
        slides.append(slide_productos)
    
    context = {
        'slides': slides,
        'productos': productos
    }
    return render(request, 'accion/layout.html', context)

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

def carrito_view(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/gracias.html', context)

def dashboard(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/dashboard.html', context)

#Configuracion admin

def configuracion(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/configuracion.html', context)


def configuracion_admin(request):
    admin = Administrador.objects.first()
    if request.method == 'POST':
        form = AdministradorForm(request.POST, request.FILES, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('configuracion')
    else:
        form = AdministradorForm(instance=admin)

    return render(request, 'accion/configuracion.html', {'form': form, 'admin': admin})

#Proveedor

def proveedores_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'accion/proveedores_list.html', {'proveedores': proveedores})

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores_list')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'accion/editar.html', {'form': form})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedores_list')
    return render(request, 'accion/eliminar.html', {'proveedor': proveedor})

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores_list')
    else:
        form = ProveedorForm()
    return render(request, 'accion/agregar.html', {'form': form})
