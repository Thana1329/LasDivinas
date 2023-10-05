from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path('', views.home),
    path('login-Registro/', views.Login, name="Login"),
	]