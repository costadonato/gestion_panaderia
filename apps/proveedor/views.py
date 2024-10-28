from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.pedido.models import MateriaPrima
from apps.proveedor.forms import NuevoProveedorForm, ModificarProveedorForm
from apps.proveedor.models import Proveedor


def lista_proveedor(request):
    proveedor = Proveedor.objects.all()
    return render(request, 'proveedor/lista_proveedor.html', {'proveedor': proveedor})

def nuevo_proveedor(request):
    if request.method == 'POST':
        form = NuevoProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('proveedor:lista_proveedor'))
    else:
        form = NuevoProveedorForm()
    return render(request, 'proveedor/proveedor_form.html', {'form': form})

def editar_proveedor(request, pk):
    materia = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ModificarProveedorForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Materia Prima actualizada correctamente')
            return redirect(reverse('proveedor:lista_proveedor'))
    else:
        form = ModificarProveedorForm(instance=materia)
    return render(request, 'proveedor/proveedor_form.html', {'form': form})

def eliminar_proveedor(request):
    if request.method == 'POST':
        if 'id_proveedor' in request.POST:
            proveedor = get_object_or_404(Proveedor, pk=request.POST['id_proveedor'])
            nombre_proveedor = proveedor.nombre
            proveedor.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Anuncio {}'.format(nombre_proveedor))
        else:
            messages.error(request, 'Debe indicar qué Proveedor se desea eliminar')
    return redirect(reverse('proveedor:lista_proveedor'))

def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, id=pk)  # Obtener la venta específica
    mat_primas_suministradas = MateriaPrima.objects.filter(proveedor=proveedor)  # Obtener los items relacionados a esta venta
    return render(request, 'proveedor/detalle_proveedor.html', {'proveedor': proveedor, 'mat_primas_suministradas':mat_primas_suministradas})