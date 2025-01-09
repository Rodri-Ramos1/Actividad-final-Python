from django.db import models
from usuarios .models import Usuario

# Create your models here.
class Proyecto(models.Model):
    nombreProyecto = models.CharField(max_length=300, null=False)
    descripcion = models.TextField(max_length=600)
    urlRepositorio = models.URLField(max_length=400)
    fechaCreacion = models.DateField(null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)




