from django.db import models
from usuarios .models import Usuario

# Create your models here.
class Habilidad (models.Model):
    nombreHabilidad = models.CharField(max_length=300, null=False)
    nivel = models.CharField(max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
