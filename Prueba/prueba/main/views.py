from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm

def home(request):
    form = RegistroUsuarioForm()
    return render(request, "index.html", {'form': form})


def productos(request):
    return render(request, "productos.html")

def contacto(request):
    return render(request, "contactos.html")

from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'login-Registro.html', {'form': form})