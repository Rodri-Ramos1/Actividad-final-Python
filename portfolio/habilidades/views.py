from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Habilidad

def lista_habilidades(request):
    habilidades = Habilidad.objects.all()

    habilidades_data = [
        {   "id" : habilidad.id,
            "nombreHabilidad" : habilidad.nombreHabilidad,
            "nivel" : habilidad.nivel,

        }
        for habilidad in habilidades
    ]
    return JsonResponse(habilidades_data, safe=False)