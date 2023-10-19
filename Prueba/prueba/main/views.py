from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm, AgregarproductosForm, CategoriaForm
from .models import Productos, Categoria

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
        form = AgregarproductosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el producto en la base de datos
            return redirect('main:productos')
    else:
        form = AgregarproductosForm()
    
    categorias = Categoria.objects.all()  # Obtén todas las categorías
    return render(request, "agregar-productos.html", {"form": form, "categorias": categorias})


def detallesproductos(request):
    detalles_productos = {
     'product_name': 'Air Jordan 1 Zoom CMFT 2',
        # Otros datos de detalles_productos aquí
    }
    return render(request, 'detalles-productos.html', {'detalles_productos': detallesproductos})


def agregarcategoria(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos del formulario en la base de datos
            return redirect('main:productos')
    else:
        form = CategoriaForm()

     
    return render(request, 'agregar-categoria.html', {"form": form, "categorias": categorias})


def editarcategoria(request):
    categorias = Categoria.objects.all()  # Recupera todas las categorías de la base de datos

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria_id = form.cleaned_data['categoria']  # Recupera la categoría seleccionada del formulario
            categoria = Categoria.objects.get(id=categoria_id)  # Inicializa la variable 'categoria'

            # Actualiza los campos de la categoría con los valores del formulario
            categoria.name = form.cleaned_data['name']
            categoria.description = form.cleaned_data['description']

            # Guarda la categoría actualizada en la base de datos
            categoria.save()

            return redirect('main:agregar-categoria')  # Redirigir a la lista de categorías o a donde sea necesario
    else:
        form = CategoriaForm()

    return render(request, 'editar-categoria.html', {"form": form, "categorias": categorias})
