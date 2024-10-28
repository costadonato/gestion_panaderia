from django.db import models

# Create your models here.
class Producto(models.Model):
    UNIDAD_MEDIDA_CHOICES = [
        ('kg', 'Kilogramos'),
        ('unid', 'Unidades')
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


    def venta_producto(self, cant):
        if self.cantidad >= cant:
            self.cantidad -= cant
            print("VENIDO")
        else:
            print("NO SE CUENTA CON STOCK SUFICIENTE")


    def aumento_stock(self, cant):
            self.cantidad += cant
            print("STOCK ACTUALIZADO")

    def dar_baja(self):
        self.estado = False

    """
    PREGUNTAR
    No escribo la función modificar, ya que intuimos que estas funciones 
    deberían ser views y no métodos de la clase Producto. 
    """
