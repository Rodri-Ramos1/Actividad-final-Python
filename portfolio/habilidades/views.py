from django.shortcuts import render
from django.http import JsonResponse
from .models import Habilidad

# Create your views here.
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