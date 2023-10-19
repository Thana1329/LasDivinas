from django.contrib import admin
from .models import registroUsuario, Productos, Categoria

# Register your models here.
admin.site.register(registroUsuario)
admin.site.register(Productos)
admin.site.register(Categoria)
