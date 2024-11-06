from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from apps.pedido.forms import NuevaMateriaPrimaForm, ModificarMateriaPrimaForm, NuevoPedidoForm, ItemPedidoFormSet, \
    Recepcion_pedido
from apps.pedido.models import MateriaPrima, Pedido, ItemPedido


@login_required(login_url='usuario:login')
@permission_required('pedido.view_materiaprima', raise_exception=True)
def lista_materia_prima(request):
    materia_prima = MateriaPrima.objects.all()[:50]
    return render(request, 'pedido/lista_materia_prima.html', {'materia_prima': materia_prima})


@login_required(login_url='usuario:login')
@permission_required('pedido.add_materiaprima', raise_exception=True)
def nueva_materia_prima(request):
    if request.method == 'POST':
        form = NuevaMateriaPrimaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pedido:lista_materia_prima'))
    else:
        form = NuevaMateriaPrimaForm()
    return render(request, 'pedido/materia_prima_form.html', {'form': form})


@login_required(login_url='usuario:login')
@permission_required('pedido.change_materiaprima', raise_exception=True)
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


@login_required(login_url='usuario:login')
@permission_required('pedido.delete_materiaprima', raise_exception=True)
def eliminar_materia_prima(request):
    if request.method == 'POST':
        materia_id = request.POST.get('id_materia')
        materia = get_object_or_404(MateriaPrima, pk=materia_id)
        nombre_materia = materia.nombre
        materia.delete()
        messages.success(request, f'Se ha eliminado {nombre_materia} exitosamente')
    return redirect(reverse('pedido:lista_materia_prima'))


@login_required(login_url='usuario:login')
@permission_required('pedido.view_pedido', raise_exception=True)
def lista_pedidos(request):
    pedidos = Pedido.objects.all()[:50]
    return render(request, 'pedido/lista_pedidos.html', {'pedidos': pedidos})


@login_required(login_url='usuario:login')
@permission_required('pedido.add_pedido', raise_exception=True)
def nuevo_pedido(request):
    pedido = None
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


@login_required(login_url='usuario:login')
@permission_required('pedido.view_pedido', raise_exception=True)
def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)  # Obtener la venta específica
    items = ItemPedido.objects.filter(pedido=pedido)  # Obtener los items relacionados a esta venta
    return render(request, 'pedido/detalle_pedido.html', {'pedido': pedido, 'items':items})

def recepcion_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    items = ItemPedido.objects.filter(pedido=pedido)

    if request.method == 'POST':
        recepcion_form = Recepcion_pedido(request.POST)
        if recepcion_form.is_valid():
            recepcion = recepcion_form.save(commit=False)
            #Agrego a la recepcion el pedido y el empleado que hizo la recepcion
            recepcion.pedido = pedido
            recepcion.empleado = request.user.empleado
            recepcion.save()

            #Cambio estado del pedido a RECIBIDO
            recepcion.pedido.estado_recibido = True
            recepcion.pedido.save()

            #actualizo materia prima
            for item in items:
                item.materia_prima.cant_disponible += item.cantidad
                item.materia_prima.save()

            messages.success(request, 'Se ha actualizado correctamente la recepcion')
            return redirect(reverse('pedido:lista_pedidos'))
    else:
        recepcion_form = Recepcion_pedido()

    return render(request, 'pedido/recepcion_pedido_form.html', {'pedido': pedido, 'form': recepcion_form})