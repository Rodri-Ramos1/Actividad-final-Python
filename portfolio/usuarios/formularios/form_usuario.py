from django import forms
from ..models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password', 'descripcion', 'telefono', 'domicilio', 'pais', 'provincia', 'ciudad', 'fechaNacimiento', 'numeroDocumento']