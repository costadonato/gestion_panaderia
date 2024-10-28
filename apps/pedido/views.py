# apps/materia_prima/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from apps.pedido.forms import NuevaMateriaPrimaForm, ModificarMateriaPrimaForm, NuevoPedidoForm, ItemPedidoFormSet
from apps.pedido.models import MateriaPrima, Pedido, ItemPedido


def lista_materia_prima(request):
    materia_prima = MateriaPrima.objects.all()
    return render(request, 'pedido/lista_materia_prima.html', {'materia_prima': materia_prima})

def nueva_materia_prima(request):
    if request.method == 'POST':
        form = NuevaMateriaPrimaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pedido:lista_materia_prima'))
    else:
        form = NuevaMateriaPrimaForm()
    return render(request, 'pedido/materia_prima_form.html', {'form': form})

def editar_materia_prima(request, pk):
    materia = get_object_or_404(MateriaPrima, pk=pk)
    if request.method == 'POST':
        form = ModificarMateriaPrimaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Materia Prima actualizada correctamente')
            return redirect(reverse('pedido:lista_materia_prima'))
    else:
        form = ModificarMateriaPrimaForm(instance=materia)
    return render(request, 'pedido/materia_prima_form.html', {'form': form})

def eliminar_materia_prima(request):
    if request.method == 'POST':
        materia_id = request.POST.get('id_materia')
        materia = get_object_or_404(MateriaPrima, pk=materia_id)
        nombre_materia = materia.nombre
        materia.delete()
        messages.success(request, f'Se ha eliminado {nombre_materia} exitosamente')
    return redirect(reverse('pedido:lista_materia_prima'))

def nuevo_pedido(request):
    pedido_nuevo = None
    monto_total = 0
    if request.method == 'POST':
        pedido_form = NuevoPedidoForm(request.POST) #request.post es un objeto del tipo diccionario
        if pedido_form.is_valid():
            pedido = pedido_form.save(commit=False)
            formset = ItemPedidoFormSet(request.POST, instance=pedido)
            if formset.is_valid():
                items = formset.save(commit=False)
                for item in items:
                    # Calcular el monto total del pedido y el de cada item individual
                    if item.precio_unid:
                        item.precio_total = item.cantidad * item.precio_unid
                        monto_total = monto_total + item.precio_total
                pedido.monto_total = monto_total
                pedido.save()

                for item in items:
                    item.save()
                return redirect('pedido:lista_pedidos')  # Redirige a la lista de pedidos después de guardar los items

    else:
        form = NuevoPedidoForm()
        formset = ItemPedidoFormSet()

    return render(request, 'pedido/pedido_form.html', {
        'form': form,
        'formset': formset
    })


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/lista_pedidos.html', {'pedidos': pedidos})

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)  # Obtener la venta específica
    items = ItemPedido.objects.filter(pedido=pedido)  # Obtener los items relacionados a esta venta
    return render(request, 'pedido/detalle_pedido.html', {'pedido': pedido, 'items':items})