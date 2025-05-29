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
            return redirect('home.html')  # mejor usar redirect a la url con nombre 'home'
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
