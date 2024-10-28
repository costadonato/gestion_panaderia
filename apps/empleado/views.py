from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.empleado.forms import EmpleadoForm
from apps.empleado.models import Empleado



# Create your views here.
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/listar_empleados.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado:listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/empleado_form.html', {'form': form})

def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado:listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'empleado/empleado_form.html', {'form': form})

def eliminar_empleado(request):
    if request.method == 'POST':
        if 'id_empleado' in request.POST:
            empleado = get_object_or_404(Empleado, pk=request.POST['id_empleado'])
            nombre_empleado = empleado.nombre_completo
            empleado.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Anuncio {}'.format(nombre_empleado))
        else:
            messages.error(request, 'Debe indicar qué empleado que se desea eliminar')
    return redirect(reverse('empleado:listar_empleados'))