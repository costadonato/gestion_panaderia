from django.urls import path
from . import views

app_name = 'empleado'
urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    path('nuevo/', views.crear_empleado, name='crear_empleado'),
    path('editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
]