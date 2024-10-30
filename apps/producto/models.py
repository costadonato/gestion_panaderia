from django.db import models

# Create your models here.
class Producto(models.Model):
    UNIDAD_MEDIDA_CHOICES = [
        ('Kg', 'Kilogramos'),
        ('U', 'Unidades')
    ]

    TIPO_CHOICES = [
        ('pasteleria', 'Pasteleria'),
        ('panaderia', 'Panaderia')
    ]

    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.CharField(max_length=500)
    unidadMedida = models.CharField(max_length=4, choices=UNIDAD_MEDIDA_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    cantidadMinima = models.PositiveIntegerField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

