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
    categorias = [(c.id, c.name) for c in Categoria.objects.all()]  # Recupera las categorías desde la base de datos
    categoria = forms.ChoiceField(choices=categorias, required=False)  # Opciones para el campo "categoria"
    name = forms.CharField()
    description = forms.CharField()

    class Meta:
        model = Categoria
        fields =('name','description','categoria', )


