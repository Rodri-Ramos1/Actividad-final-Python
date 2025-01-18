from django.urls import path
from . import views

urlpatterns = [
    path('estudios/', views.lista_estudios, name = 'lista_estudios')
]