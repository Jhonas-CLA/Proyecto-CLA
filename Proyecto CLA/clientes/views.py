from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})




def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/agregar_cliente.html', {'form': form})



def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})



def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('listar_clientes')




# Create your views here.
