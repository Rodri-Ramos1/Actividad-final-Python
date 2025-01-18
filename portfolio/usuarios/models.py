from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=300, null=False)
    email = models.CharField(max_length=300, null=False)
    password = models.CharField(max_length=300, null=False)
    descripcion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=20)
    domicilio = models.CharField(max_length= 500)
    pais = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=250)
    fechaNacimiento = models.DateField(null=False)
    numeroDocumento = models.CharField(max_length=50)



