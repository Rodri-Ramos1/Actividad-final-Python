from django.db import models
from usuarios .models import Usuario

# Create your models here.
class Estudio (models.Model):
    nombreEstudio = models.CharField(max_length=300, null=False)
    nombreInstitucion = models.CharField(max_length=500, null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)