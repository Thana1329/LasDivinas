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
    
class productos(models.Model):

    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'
        ordering = ["name"]

    CATEGORIAS_CHOICES = [
    ('prenda superior', 'Prenda Superior'),
    ('prenda inferior', 'Prenda Inferior'),
    ('zapatillas', 'Zapatillas'),
    ('laptops', 'Laptops'),
    ('celulares', 'Celulares'),
    ('audifonos', 'Audifonos'),
]
       
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="productos")
    category = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(productos, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/productos/{self.slug}"
