from django.urls import path
from apps.proveedor import views

app_name = 'proveedor'
urlpatterns = [
    path('', views.lista_proveedor, name='lista_proveedor'),
    path('nuevo/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('detalle/<int:pk>/', views.detalle_proveedor, name='detalle_proveedor'),
]