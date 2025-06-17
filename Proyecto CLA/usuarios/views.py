from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm
from django.contrib import messages


# ******** CONTROL DE INGRESO DE USUARIOS ***********************************************************
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)

            # Redirige según el tipo de usuario
            if user.is_superadmin or user.is_staff:
                return redirect('dashboard')  # esta URL debe existir en tu urls.py
            else:
                return redirect('home')  # cambia por tu vista de inicio para usuarios normales

        else:
            return render(request, 'usuarios/login.html', {'alarma': 'Correo o contraseña no válida!'})
    else:
        return render(request, 'usuarios/login.html')


# ********* CIERRE DE SESIÓN DEL USUARIO **********************************************************
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


# ********* REGISTRO DE NUEVO USUARIO *************************************************************
def registrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('registro')
        else:
            messages.error(request, 'Por favor revisa los campos y vuelve a intentarlo')
    else:
        form = UsuarioForm()
    return render(request, 'accion/registro.html', {'form': form})

#******DASHBOARD******************#
from django.contrib.auth.decorators import user_passes_test

def es_admin(user):
    return user.is_authenticated and (user.is_superadmin or user.is_staff)

@user_passes_test(es_admin, login_url='login')
def dashboard(request):
    return render(request, 'admin/dashboard.html')  # usa tu template de dashboard
