from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import  AgregarproductosForm, CategoriaForm, CustomUserCreationForm
from .models import Productos, Categoria
from django.http import HttpResponse
from django.views import generic



@login_required
def home(request):
    return render(request, "index.html")


def productosvistas(request): 
    categorias = Categoria.objects.all()
    categorias_con_productos = {}  # Un diccionario para almacenar las categorías y sus productos asociados

    for categoria in categorias:
        productos = Productos.objects.filter(category=categoria)  # Filtrar productos por categoría
        categorias_con_productos[categoria] = productos

    return render(request, 'productos.html', {'categorias_con_productos': categorias_con_productos})

    

def contacto(request):
    return render(request, "contactos.html")

def categoriavistas(request):
    categorias = Categoria.objects.all()
    productos = Productos.objects.all()

    return render(request, 'categorias.html', {'categorias': categorias, 'productos': productos})




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

def cargar_producto(producto_id):
    try:
        return Productos.objects.get(id=producto_id)
    except Productos.DoesNotExist:
        return None

def editarproducto(request):
    producto_id = None
    if request.method == 'POST':
        producto_id = request.POST.get('product_select')  # Obtener el producto seleccionado
        producto = cargar_producto(producto_id)  # Cargar el producto a editar

        # Crear un formulario con los datos del producto
        if producto is not None:
            form = AgregarproductosForm(request.POST, request.FILES, instance=producto)

            if form.is_valid():
                form.save()  # Guardar los cambios en el producto
                return redirect('main:productos')
  # Redirigir a la página de lista de productos o donde desees

    else:
        form = AgregarproductosForm(instance=None)

    # Obtener la lista de productos y categorías para llenar los formularios
    productos = Productos.objects.all()
    categorias = Categoria.objects.all()

    # Resto del código para mostrar el formulario de selección del producto
    # y el formulario de edición

    context = {
        'form': form,
        'producto_id': producto_id,
        'productos': productos,
        'categorias': categorias,
    }

    return render(request, 'editar-productos.html', context)

def eliminarproducto(request):
    mensaje_error = None
    if request.method:
        producto_id = request.POST.get('producto_id')
        try:
            producto = Productos.objects.get(pk=producto_id)
            producto.delete()
            return redirect('main:productos')
        except Productos.DoesNotExist:
            mensaje_error = "La categoria seleccionada no existe."
    productos = Productos.objects.all()
    return render(request, 'eliminar-productos.html', {"productos": productos})
    
               


def detallesproductos(request, producto_id):
    producto = get_object_or_404(Productos, pk=producto_id)
    if request.method == 'POST':
        form = AgregarproductosForm(request.POST)
        if form.is_valid():
            return redirect('producto', producto_id = producto_id)
    else:
        form = AgregarproductosForm()
    return render(request, 'detalles-productos.html', {'producto': producto})




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

def eliminarcategoria(request):
    mensaje_error = None

    if request.method == 'POST':
        categoria_id = request.POST.get('categoria_id')
        try:
            categoria = Categoria.objects.get(pk=categoria_id)
            categoria.delete()
            return redirect('main:agregar-categoria')
        except Categoria.DoesNotExist:
            mensaje_error = "La categoria seleccionada no existe."
    categorias = Categoria.objects.all()
    return render(request, 'eliminar-categoria.html', {'categorias': categorias})

def registro(request):
    data = {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"]) 
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="login")
        data['form'] = formulario
    return render(request, 'registration/registro.html',data)

