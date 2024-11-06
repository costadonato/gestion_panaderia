from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.pedido.models import MateriaPrima
from apps.proveedor.forms import NuevoProveedorForm, ModificarProveedorForm
from apps.proveedor.models import Proveedor

@login_required(login_url='usuario:login')
@permission_required('proveedor.view_proveedor', raise_exception=True)
def lista_proveedor(request):
    proveedor = Proveedor.objects.all()[:50]
    return render(request, 'proveedor/lista_proveedor.html', {'proveedor': proveedor})


@login_required(login_url='usuario:login')
@permission_required('proveedor.add_proveedor', raise_exception=True)
def nuevo_proveedor(request):
    if request.method == 'POST':
        form = NuevoProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('proveedor:lista_proveedor'))
    else:
        form = NuevoProveedorForm()
    return render(request, 'proveedor/proveedor_form.html', {'form': form})


@login_required(login_url='usuario:login')
@permission_required('proveedor.change_proveedor', raise_exception=True)
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


@login_required(login_url='usuario:login')
@permission_required('delete.view_proveedor', raise_exception=True)
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


@login_required(login_url='usuario:login')
@permission_required('proveedor.view_proveedor', raise_exception=True)
def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, id=pk)  # Obtener la venta específica
    mat_primas_suministradas = MateriaPrima.objects.filter(proveedor=proveedor)  # Obtener los items relacionados a esta venta
    return render(request, 'proveedor/detalle_proveedor.html', {'proveedor': proveedor, 'mat_primas_suministradas':mat_primas_suministradas})