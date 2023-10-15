from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm
from .forms import agregarproductosForm
from .models import productos

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


    return render(request, "agregar-productos.html")

def agregarproducto(request):
    if request.method == "POST":
        form = agregarproductosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:productos')
    else:
        form = agregarproductosForm()
    return render(request, "agregar-productos.html", {"form": form})

def detallesproductos(request):
    detalles_productos = {
     'product_name': 'Air Jordan 1 Zoom CMFT 2',
        # Otros datos de detalles_productos aquí
    }
    return render(request, 'detalles-productos.html', {'detalles_productos': detallesproductos})