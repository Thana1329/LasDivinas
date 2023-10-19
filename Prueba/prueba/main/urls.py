from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path('', views.home, name="home"),
    path('login-Registro/', views.registrar_usuario, name="login-Registro"),
    path('productos/', views.productosvistas, name="productos"),
    path('contactos/', views.contacto, name="contactos"),
    path('categorias/', views.categoriavistas, name="categorias"),
    path('agregar-productos/', views.agregarproducto, name="agregar-productos"),
    path('editar-productos/', views.editarproducto, name='editar-productos'),
    path('eliminar-productos/', views.eliminarproducto, name='eliminar-productos'),
    path('producto/<int:producto_id>/', views.detallesproductos, name='producto'),
    path('agregar-categoria/', views.agregarcategoria, name="agregar-categoria"),
    path('editar-categoria/', views.editarcategoria, name='editar-categoria'),
    path('eliminar-categoria/', views.eliminarcategoria , name="eliminar-categoria"),
	]