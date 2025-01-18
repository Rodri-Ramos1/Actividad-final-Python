from django.urls import path
from . import views

urlpatterns = [
    path('habilidades/', views.lista_habilidades, name = 'lista_habilidades')
]
