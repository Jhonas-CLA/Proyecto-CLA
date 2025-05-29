from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import LoginForm
from django.contrib import messages
from usuarios.forms import CustomUserCreationForm  

def registro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home/')  # O cambia por una vista que tengas
    else:
        form = CustomUserCreationForm()
    return render(request, 'accion/registro.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accion/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f'Bienvenido {usuario.username}')
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  
    else:
        form = AuthenticationForm()
    return render(request, 'accion/inicioSesion.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contrasena = form.cleaned_data['contrasena']
            user = authenticate(request, username=usuario, password=contrasena)
            if user is not None:
                login(request, user)
                return redirect('home')  # Cambia por la vista que desees
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})