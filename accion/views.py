from .models import Interfaz
from .models import Producto 
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Administrador

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


#Vista del administrador

def guardar_configuracion(request):
    if request.method == 'POST':
        try:
            admin = Administrador.objects.get(user=request.user)
        except Administrador.DoesNotExist:
            admin = Administrador(user=request.user)

        admin.nombre_completo = request.POST.get('nombre_completo')
        admin.correo = request.POST.get('correo')
        admin.telefono = request.POST.get('telefono')
        admin.direccion = request.POST.get('direccion')
        admin.nombre_local = request.POST.get('nombre_local')
        admin.nit = request.POST.get('nit')
        admin.direccion_local = request.POST.get('direccion_local')
        admin.notificaciones = 'notificaciones' in request.POST

        if 'foto' in request.FILES:
            admin.foto = request.FILES['foto']

        admin.save()

        # 🔁 Redirigir para recargar el admin en el formulario
        return redirect('configuracion')


    
def configuracion_admin(request):
    try:
        admin = Administrador.objects.get(user=request.user)
    except Administrador.DoesNotExist:
        admin = Administrador(user=request.user)
    return render(request, 'accion/configuracion.html', {'admin': admin})

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

def dashboard(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/dashboard.html', context)

def configuracion(request):
    interfaz=Interfaz.objects.all()
    context={'interfaz':interfaz}
    return render(request, 'accion/configuracion.html', context)
