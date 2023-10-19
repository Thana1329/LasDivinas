from django.contrib import admin
from .models import Productos, Categoria, Resena

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categoria)
admin.site.register(Resena)