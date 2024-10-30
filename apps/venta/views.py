from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.venta.forms import NuevaVentaForm, ItemFormSet
from apps.venta.models import Venta, Item


@login_required(login_url='usuario:login')
@permission_required('venta.view_venta', raise_exception=True)
def lista_ventas(request):
    ventas = Venta.objects.all()  # Obtener todas las ventas
    return render(request, 'venta/lista_ventas.html', {'ventas': ventas})


@login_required(login_url='usuario:login')
@permission_required('venta.add_venta', raise_exception=True)
def nueva_venta(request):
    venta = None
    monto_total = 0
    if request.user.empleado:
        if request.method == 'POST':
            venta_form = NuevaVentaForm(request.POST) #request.post es un objeto del tipo diccionario
            if venta_form.is_valid():
                venta = venta_form.save(commit=False)
                venta.empleado = request.user.empleado
                formset = ItemFormSet(request.POST, instance=venta)
                if formset.is_valid():
                    items = formset.save(commit=False)
                    for item in items:
                        # Calcular el monto total de la venta y el de cada item individual
                        if item.producto:
                            item.precio_item = item.cantidad * item.producto.precio
                            monto_total = monto_total + item.precio_item
                    venta.monto_total = monto_total
                    venta.save()

                    for item in items:
                        item.save()
                        item.producto.cantidad -= item.cantidad
                        item.producto.save()
                    return redirect('venta:lista_ventas')  # Redirige a la lista de ventas después de guardar los items

        else:
            form = NuevaVentaForm()
            formset = ItemFormSet()

    return render(request, 'venta/venta_form.html', {
        'form': form,
        'formset': formset
    })


@login_required(login_url='usuario:login')
@permission_required('venta.view_venta', raise_exception=True)
def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)  # Obtener la venta específica
    items = Item.objects.filter(venta=venta)  # Obtener los items relacionados a esta venta
    return render(request, 'venta/detalle_venta.html', {'venta': venta, 'items':items})
