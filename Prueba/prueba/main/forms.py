from django import forms
from .models import registroUsuario
from .models import productos

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = registroUsuario
        fields = ['nombre', 'email', 'usuario', 'contrasena']

class agregarproductosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = ('name', 'description', 'price', 'slug')	

