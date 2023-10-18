from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path('', views.home, name="home"),
    path('login-Registro/', views.registrar_usuario, name="login-Registro"),
    path('productos/', views.productos, name="productos"),
    path('contactos/', views.contacto, name="contactos"),
    path('agregar-productos/', views.agregarproducto, name="agregar-productos"),
    path('detalles-productos/', views.detallesproductos, name="detalles-productos"),
    path('agregar-categoria/', views.agregarcategoria, name="agregar-categoria"),
    path('editar-categoria/', views.editarcategoria, name='editar-categoria'),
	]