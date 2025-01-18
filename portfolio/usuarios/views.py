from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Usuario
from .formularios.form_usuario import UsuarioForm

# Create your views here.

def lista_usuarios(request): 
    usuarios = Usuario.objects.all()

    usuarios_data = [
        {   "id" : usuario.id,
            "nombre" : usuario.nombre,
            "email" : usuario.email,
            "password" : usuario.password,
            "descrpcion" : usuario.descripcion,
            "telefono" : usuario.telefono,
            "domicilio" : usuario.domicilio,
            "pais" : usuario.pais,
            "provincia" : usuario.provincia,
            "ciudad" : usuario.ciudad,
            "fechaNacimiento" : usuario.fechaNacimiento,
            "numeroDocumento" : usuario.numeroDocumento,
            }
            for usuario in usuarios
    ]
    return JsonResponse(usuarios_data, safe = False)

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(lista_usuarios)
    else:
        form = UsuarioForm()
    
    return render (request, 'crear_usuario.html', {"form" : form})