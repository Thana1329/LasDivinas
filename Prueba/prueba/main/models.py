from django.db import models
from django.urls import reverse

class registroUsuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length=255, unique=True)
    contrasena = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('index')
