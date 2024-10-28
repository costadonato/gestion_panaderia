from django.db import models


class ClienteMayorista(models.Model):
    nombre_completo = models.CharField(max_length=100)
    cuit = models.CharField(max_length=13, unique=True)
    activo = models.BooleanField(default=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    domicilio_calle = models.CharField(max_length=100)
    domicilio_numero = models.IntegerField()
    domicilio_localidad = models.CharField(max_length=50)
    domicilio_departamento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_completo

