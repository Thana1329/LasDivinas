from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def Login(request):
    return render(request, "login-Registro.html")


