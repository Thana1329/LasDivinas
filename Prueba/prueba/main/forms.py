from django import forms
from .models import registroUsuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = registroUsuario
        fields = ['nombre', 'email', 'usuario', 'contrasena']

