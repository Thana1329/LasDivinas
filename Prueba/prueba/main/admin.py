from django.contrib import admin
from .models import registroUsuario, productos, categoria

# Register your models here.
admin.site.register(registroUsuario)
admin.site.register(productos)
admin.site.register(categoria)
