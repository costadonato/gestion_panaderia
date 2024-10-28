from django.urls import path

from apps.venta import views

app_name = 'venta'
urlpatterns = [
    path('', views.lista_ventas, name='lista_ventas'),  # Listar ventas
    path('<int:venta_id>/', views.detalle_venta, name='detalle_venta'),  # Detalle de venta
    path('nueva/',views.nueva_venta,name='nueva_venta'),
    #path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    #path('eliminar/', views.eliminar_producto, name='eliminar_producto' )
]