from django import forms
from .models import registroUsuario, Productos, Categoria

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = registroUsuario
        fields = ['nombre', 'email', 'usuario', 'contrasena']

class AgregarproductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('name', 'description', 'price', 'image', 'category')	

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields =('name','description',)

