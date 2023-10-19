from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class registroUsuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length=255, unique=True)
    contrasena = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('index')
    


class Categoria(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Nombre de la categoría
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Productos(models.Model):
    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'
        ordering = ["name"]

    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, null=True, upload_to="productos")
    category = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)  # Vinculación a la categoría

    def __str__(self):
        return self.name
