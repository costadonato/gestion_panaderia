from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.venta.forms import NuevaVentaForm, ItemFormSet
from apps.venta.models import Venta, Item


# Create your views here.

def nueva_venta(request):
    venta_nueva = None
    monto_total = 0
    if request.method == 'POST':
        venta_form = NuevaVentaForm(request.POST) #request.post es un objeto del tipo diccionario
        if venta_form.is_valid():
            venta = venta_form.save(commit=False)
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

def lista_ventas(request):
    ventas = Venta.objects.all()  # Obtener todas las ventas
    return render(request, 'venta/lista_ventas.html', {'ventas': ventas})

def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)  # Obtener la venta específica
    items = Item.objects.filter(venta=venta)  # Obtener los items relacionados a esta venta
    return render(request, 'venta/detalle_venta.html', {'venta': venta, 'items':items})
