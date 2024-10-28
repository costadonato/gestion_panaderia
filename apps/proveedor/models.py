from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length= 200)
    domicilioCalle = models.CharField(max_length=100)
    domicilioNum = models.PositiveIntegerField()
    domicilioLocalidad = models.CharField(max_length=100)
    domicilioDepartamento = models.CharField(max_length=100)
    razonSocial = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre