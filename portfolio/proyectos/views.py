from django.shortcuts import render
from django.http import JsonResponse 
from .models import Proyecto 

# Create your views here.
def lista_proyectos(request): 
    proyectos = Proyecto.objects.all()
    
    proyectos_data = [
        {   "id" : proyecto.id,
            "nombreProyecto" : proyecto.nombreProyecto,
            "descripcion" : proyecto.descripcion,
            "urlRepositorio" : proyecto.urlRepositorio,
            "fechaCreacion" : proyecto.fechaCreacion,
            
        }
        for proyecto in proyectos

     ]
    return JsonResponse(proyectos_data, safe=False)