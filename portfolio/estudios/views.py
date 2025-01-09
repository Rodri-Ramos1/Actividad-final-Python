from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Estudio

def lista_estudios(request):
    estudios = Estudio.objects.all()

    estudios_data = [
        {   "id" : estudio.id,
            "nombreEstudio" : estudio.nombreEstudio,
            "nombreInstitucion" : estudio.nombreInstitucion,

        }
        for estudio in estudios
    ]
    return JsonResponse(estudios_data, safe=False)