from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse 
from .models import Proyecto 

"""def lista_proyectos(request): 
    proyectos = Proyecto.objects.all() 
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})""" 

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