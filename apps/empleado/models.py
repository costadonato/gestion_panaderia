from django.db import models


class Empleado(models.Model):
    estado = models.BooleanField(default=True)
    cuit = models.CharField(max_length=13, unique=True)
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    fecha_incorporacion = models.DateField()
    domicilio_calle = models.CharField(max_length=100)
    domicilio_numero = models.IntegerField()
    domicilio_localidad = models.CharField(max_length=50)
    domicilio_departamento = models.CharField(max_length=50)
    usuario = models.OneToOneField('usuario.Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo


