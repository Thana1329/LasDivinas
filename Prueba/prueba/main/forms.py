from django import forms
from .models import registroUsuario, productos, categoria

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = registroUsuario
        fields = ['nombre', 'email', 'usuario', 'contrasena']

class agregarproductosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = ('name', 'description', 'price', 'image', 'category')	

class categoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields =('name',)

