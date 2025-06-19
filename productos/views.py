from django.shortcuts import render
from .models import Producto

def carrito_view(request):
    productos = Producto.objects.all()
    return render(request, 'productos/carrito.html', {'productos': productos})

# productos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    return render(request, 'productos/productos_list.html', {
        'productos': productos,
        'form': form
    })

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('listar_productos')

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('listar_productos')