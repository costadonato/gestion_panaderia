from django.urls import path
from apps.pedido import views
from apps.pedido.models import RecepcionPedido

app_name = 'materia_prima'
urlpatterns = [
    path('', views.lista_materia_prima, name='lista_materia_prima'),
    path('nuevo/', views.nueva_materia_prima, name='nueva_materia_prima'),
    path('editar/<int:pk>/', views.editar_materia_prima, name='editar_materia_prima'),
    path('eliminar/', views.eliminar_materia_prima, name='eliminar_materia_prima'),
    path('nuevo-pedido/',views.nuevo_pedido, name='nuevo_pedido'),
    path('lista-pedidos/',views.lista_pedidos, name='lista_pedidos'),
    path('detalle-pedido/<int:pedido_id>/',views.detalle_pedido, name='detalle_pedido'),
    path('recepcion_pedido/<int:pedido_id>', views.recepcion_pedido, name='recepcion_pedido' )
]