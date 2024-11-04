from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.db.models import F, Count
from apps.pedido.models import MateriaPrima
from django.shortcuts import render
from apps.producto.models import Producto
from apps.venta.models import Venta, Item
from datetime import datetime

@login_required(login_url='usuario:login')
@user_passes_test(lambda u: u.groups.filter(name="Administrador").exists())
def informe_ventas(request):
    ventas = Venta.objects.all()[:100]
    return render(request, 'informe/informe_ventas.html', {'ventas': ventas})


@login_required(login_url='usuario:login')
@user_passes_test(lambda u: u.groups.filter(name="Administrador").exists())
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


@login_required(login_url='usuario:login')
@user_passes_test(lambda u: u.groups.filter(name="Administrador").exists())
def informe_productos_faltantes(request):
    productos = Producto.objects.all()
    productos_faltantes = productos.filter(cantidad__lt = F('cantidadMinima'))
    return render(request, 'informe/informe_productos_faltantes.html', {'productos_faltantes': productos_faltantes})


@login_required(login_url='usuario:login')
@user_passes_test(lambda u: u.groups.filter(name="Administrador").exists())
def informe_matprima_faltante(request):
    materia_prima = MateriaPrima.objects.all()
    materia_prima_faltante = materia_prima.filter(cant_disponible__lt = F('cantidadMinima'))
    return render(request, 'informe/informe_matprima_faltante.html', {'materia_prima_faltante': materia_prima_faltante})


@login_required(login_url='usuario:login')
@user_passes_test(lambda u: u.groups.filter(name="Administrador").exists())
def informe_productos_mas_vendidos(request):
    items = Item.objects.all()

    if request.method == 'POST':
        fecha_inicio = request.POST.get('fec_inicio')
        fecha_fin = request.POST.get('fec_fin')

        if fecha_inicio and fecha_fin:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
            items = items.filter(
                venta__fecha_venta__range=(fecha_inicio, fecha_fin)
            )

    # Agrupar por producto y sumar cantidades vendidas, luego ordenar y limitar a 10
    productos_vendidos = (
        items.values('producto__nombre')
        .annotate(total_vendido=Count('venta', distinct=True))  # Cuenta las ventas únicas de cada producto
        .order_by('-total_vendido')[:10]
    )

    '''
    CONSULTA EN SQL
    
    SELECT producto.nombre AS producto__nombre, COUNT(DISTINCT item.venta_id) AS total_vendido
    FROM item
    INNER JOIN producto ON item.producto_id = producto.id
    GROUP BY producto.nombre
    ORDER BY total_vendido DESC
    LIMIT 10;
    '''

    return render(request, 'informe/informe_productos_mas_vendidos.html', {'productos_vendidos': productos_vendidos})


@login_required(login_url='usuario:login')
@user_passes_test(lambda u: u.groups.filter(name="Administrador").exists())
def informe_empleados_mas_ventas(request):
    ventas = Venta.objects.all()

    if request.method == 'POST':
        fecha_inicio = request.POST.get('fec_inicio')
        fecha_fin = request.POST.get('fec_fin')

        if fecha_inicio and fecha_fin:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
            ventas = ventas.filter(fecha_venta__range=(fecha_inicio, fecha_fin))

    empleados_mas_ventas = (
        ventas.values('empleado__nombre_completo')
        .annotate(total_ventas=Count('id'))
        .order_by('-total_ventas')
    )
    return render(request, 'informe/informe_empleados_mas_ventas.html', {'empleados_mas_ventas': empleados_mas_ventas})
