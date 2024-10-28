from django.db import models

# Create your models here.

class Pedido(models.Model):
    fecha_emision = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.CharField(max_length=500)
    proveedor = models.ForeignKey('proveedor.Proveedor',on_delete=models.SET_NULL,related_name='pedidos_proveedor', blank=True, null=True)


class ItemPedido(models.Model):
    cantidad = models.PositiveIntegerField()
    precio_unid = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    pedido = models.ForeignKey('Pedido',on_delete=models.CASCADE,related_name='items_pedido')
    materia_prima = models.ForeignKey('MateriaPrima', on_delete=models.SET_NULL, related_name = 'materia_prima_pedida', blank=True, null=True)


class RecepcionPedido(models.Model):
    fecha_recepcion = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    conforme = models.BooleanField()
    observaciones = models.CharField(max_length=500)
    pedido = models.OneToOneField('Pedido', on_delete=models.CASCADE, related_name='pedido_recibido')
    empleado = models.ForeignKey('empleado.Empleado',on_delete=models.SET_NULL, related_name='pedidos_empleado', blank=True, null=True)


class ItemRecibido(models.Model):
    cantidad = models.PositiveIntegerField()
    precio_unid = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    recepcion_pedido = models.ForeignKey('RecepcionPedido', on_delete=models.CASCADE, related_name='items_recepcion_pedido')
    materia_prima = models.ForeignKey('MateriaPrima', on_delete=models.SET_NULL, related_name = 'materia_prima_recibida', blank=True, null=True)


class MateriaPrima(models.Model):
    nombre = models.CharField(max_length=100)
    cant_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey('proveedor.Proveedor', on_delete=models.SET_NULL, related_name='materia_prima_provista', blank=True, null=True)

    def __str__(self):
        return self.nombre