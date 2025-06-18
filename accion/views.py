from .models import Interfaz
from .models import Producto 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from usuarios.models import Usuario
from .forms import UsuarioForm

from .models import Administrador
from .forms import AdministradorForm

from .models import Proveedor
from .forms import ProveedorForm
# Create your views here.

def home(request):
    productos = Producto.objects.all()

    # Agrupar de 2 en 2 para cada slide del carrusel
    slides = [productos[i:i + 2] for i in range(0, len(productos), 2)]

    return render(request, 'accion/home.html', {'slides': slides})

from django.shortcuts import render
from productos.models import Producto

def layout(request):
    productos = Producto.objects.all()
    slides = [productos[i:i+2] for i in range(0, len(productos), 2)]
    return render(request, 'accion/layout.html', {'slides': slides})

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

def loginadmin(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/loginadmin.html', context)

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
    return render(request, 'accion/editarP.html', {'form': form})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedores_list')
    return render(request, 'accion/eliminarP.html', {'proveedor': proveedor})

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores_list')
    else:
        form = ProveedorForm()
    return render(request, 'accion/agregarP.html', {'form': form})

#Usuarios

def usuarios_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'accion/usuarios_list.html', {'usuarios': usuarios})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'accion/editarU.html', {'form': form})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios_list')
    return render(request, 'accion/eliminarU.html', {'usuario': usuario})

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios_list')
    else:
        form = UsuarioForm()
    return render(request, 'accion/agregarU.html', {'form': form})

#Esto es analiticas

def analiticas(request):
    return render(request, 'accion/analiticas.html')

def gestionUsuario(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/gestionUsuario.html', context)