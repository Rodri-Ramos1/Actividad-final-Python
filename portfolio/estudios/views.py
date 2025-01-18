from django.shortcuts import render
from django.http import JsonResponse
from .models import Estudio

# Create your views here.
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