from xml.dom.minidom import Document

from django.db.models import F
from django.shortcuts import render

from apps.pedido.models import MateriaPrima
from apps.producto.models import Producto
from apps.venta.models import Venta

# Create your views here.
def informe_ventas(request):
    ventas = Venta.objects.all()[:100]
    return render(request, 'informe/informe_ventas.html', {'ventas': ventas})

def informe_ventas_filtradas(request):
    ventas = Venta.objects.all()

    if request.method == 'POST':
        fecha_inicio = request.POST.get('fec_inicio')
        fecha_fin = request.POST.get('fec_fin')
        tipo_cliente = request.POST.get('tipo_cliente')
        forma_pago = request.POST.get('forma_pago')

        if fecha_inicio and fecha_fin:
            ventas = ventas.filter(fecha_venta__range=(fecha_inicio, fecha_fin))
        if tipo_cliente:
            ventas = ventas.filter(tipo_cliente=tipo_cliente)
        if forma_pago:
            ventas = ventas.filter(forma_pago=forma_pago)

    return render(request, 'informe/informe_ventas.html', {'ventas': ventas})

def informe_productos_faltantes(request):
    productos = Producto.objects.all()
    productos_faltantes = productos.filter(cantidad__lt = F('cantidadMinima'))
    return render(request, 'informe/informe_productos_faltantes.html', {'productos_faltantes': productos_faltantes})

def informe_matprima_faltante(request):
    materia_prima = MateriaPrima.objects.all()
    materia_prima_faltante = materia_prima.filter(cant_disponible__lt = F('cantidadMinima'))
    return render(request, 'informe/informe_matprima_faltante.html', {'materia_prima_faltante': materia_prima_faltante})