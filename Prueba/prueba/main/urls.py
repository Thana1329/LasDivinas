from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path('', views.home, name="home"),
    path('login-Registro/', views.Login, name="Login"),
    path('productos/', views.productos, name="productos"),
    path('contactos/', views.contacto, name="contactos"),
	]