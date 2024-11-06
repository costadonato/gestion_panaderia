from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.cliente_mayorista.models import ClienteMayorista
from apps.cliente_mayorista.forms import NuevoClienteMayoristaForm, ModificarClienteMayoristaForm
from apps.venta.models import Venta


@login_required(login_url='usuario:login')
@permission_required('cliente_mayorista.view_cliente_mayorista', raise_exception=True)
def lista_clientesmayoristas(request):
    clientes_mayoristas = ClienteMayorista.objects.all()[:50]
    return render(request, 'cliente_mayorista/lista_clientesmayoristas.html', {'clientes_mayoristas': clientes_mayoristas})


@login_required(login_url='usuario:login')
@permission_required('cliente_mayorista.add_cliente_mayorista', raise_exception=True)
def nuevo_clientemayorista(request):
    nuevo_clientem = None
    if request.method == 'POST':
        clientemayorista_form = NuevoClienteMayoristaForm(request.POST) #request.post es un objeto del tipo diccionario
        if clientemayorista_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nuevo_clientem = clientemayorista_form.save(commit=False)
            nuevo_clientem.save()
            return redirect(reverse('cliente_mayorista:lista_clientesmayoristas'))
    else:
        clientemayorista_form = NuevoClienteMayoristaForm()

    return render(request, 'cliente_mayorista/clientemayorista_form.html', {'form': clientemayorista_form})

@login_required(login_url='usuario:login')
@permission_required('cliente_mayorista.change_cliente_mayorista', raise_exception=True)
def editar_clientemayorista(request, pk):
    clientemayorista = get_object_or_404(ClienteMayorista, pk=pk)
    if request.method == 'POST':
        clientemayorista_form = ModificarClienteMayoristaForm(request.POST, instance=clientemayorista)
        if clientemayorista_form.is_valid():
            clientemayorista_form.save(commit=True)
            messages.success(request, 'Se ha actualizado correctamente el Cliente Mayorista')
            return redirect(reverse('cliente_mayorista:lista_clientesmayoristas'))
    else:
        clientemayorista_form = ModificarClienteMayoristaForm(instance=clientemayorista)

    return render(request, 'cliente_mayorista/clientemayorista_form.html', {'form': clientemayorista_form})


@login_required(login_url='usuario:login')
@permission_required('cliente_mayorista.delete_cliente_mayorista', raise_exception=True)
def eliminar_clientemayorista(request):
    if request.method == 'POST':
        if 'id_clientemayorista' in request.POST:
            clientemayorista = get_object_or_404(ClienteMayorista, pk=request.POST['id_clientemayorista'])
            nombre_clientemayorista = clientemayorista.nombre_completo
            clientemayorista.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Cliente Mayorista {}'.format(nombre_clientemayorista))
        else:
            messages.error(request, 'Debe indicar cual Cliente Mayorista se desea eliminar')
    return redirect(reverse('cliente_mayorista:lista_clientesmayoristas'))


@login_required(login_url='usuario:login')
@permission_required('cliente_mayorista.view_cliente_mayorista', raise_exception=True)
def detalle_clientemayorista(request, pk):
    cliente = get_object_or_404(ClienteMayorista, id=pk)
    compras_realizadas = Venta.objects.filter(cliente_mayorista=cliente)  # Obtener las ventas relacionados a este cliente
    return render(request, 'cliente_mayorista/detalle_cliente.html', {'cliente': cliente, 'compras_realizadas':compras_realizadas})