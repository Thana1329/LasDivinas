from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('productos/', views.productosvistas, name="productos"),
    path('categorias/', views.categoriavistas, name="categorias"),
    path('agregar-productos/', views.agregarproducto, name="agregar-productos"),
    path('editar-productos/', views.editarproducto, name='editar-productos'),
    path('eliminar-productos/', views.eliminarproducto, name='eliminar-productos'),
    path('producto/<int:producto_id>/', views.detallesproductos, name='producto'),

    path('agregar-categoria/', views.agregarcategoria, name="agregar-categoria"),
    path('editar-categoria/', views.editarcategoria, name='editar-categoria'),
    path('eliminar-categoria/', views.eliminarcategoria , name="eliminar-categoria"),
    path('registro/', views.registro, name="registro"),
    ]
