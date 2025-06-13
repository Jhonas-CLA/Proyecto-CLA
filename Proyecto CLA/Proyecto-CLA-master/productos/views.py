from django.shortcuts import render
from .models import Producto

def carrito_view(request):
    productos = Producto.objects.all()
    return render(request, 'productos/carrito.html', {'productos': productos})
