from django.db import models

# Create your models here.

class Venta(models.Model):
    TIPO_CLIENTE_CHOICES = [
        ('Mayorista', 'Mayorista'),
        ('Final', 'Consumidor final')
    ]

    TIPO_VENTA_CHOICES = [
        ('Contado', 'Contado'),
        ('Credito', 'Crédito')
    ]

    FORMA_PAGO_CHOICES = [
        ('Tarjeta', 'Tarjeta'),
        ('Efectivo', 'Efectivo')
    ]

    tipo_cliente = models.CharField(choices=TIPO_CLIENTE_CHOICES)
    cliente_mayorista = models.ForeignKey('cliente_mayorista.ClienteMayorista', on_delete = models.SET_NULL,
                                           related_name = 'ventas_cliente_mayorista', blank=True, null=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    tipo_venta = models.CharField(choices=TIPO_VENTA_CHOICES)
    forma_pago = models.CharField(choices=FORMA_PAGO_CHOICES)
    monto_total = models.DecimalField(max_digits = 10, decimal_places = 2, blank=True, null=True)
    observaciones = models.CharField(max_length = 500)
    empleado = models.ForeignKey('empleado.Empleado', on_delete=models.SET_NULL,
                                           related_name = 'ventas_empleado', blank=True, null=True)


class Item(models.Model):
    venta = models.ForeignKey('Venta',on_delete=models.CASCADE, related_name='items_venta')
    producto = models.ForeignKey('producto.Producto', on_delete=models.SET_NULL, related_name='items_venta_producto', blank=True, null=True)
    cantidad = models.DecimalField(max_digits = 10, decimal_places = 2)
    precio_item = models.DecimalField(max_digits = 10, decimal_places = 2)

