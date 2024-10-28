from django.urls import path

from apps.cliente_mayorista import views

app_name = 'cliente_mayorista'
urlpatterns = [
    path('', views.lista_clientesmayoristas, name='lista_clientesmayoristas'),
    path('nuevo/', views.nuevo_clientemayorista,name='nuevo_clientemayorista'),
    path('editar/<int:pk>/', views.editar_clientemayorista, name='editar_clientemayorista'),
    path('eliminar/', views.eliminar_clientemayorista, name='eliminar_clientemayorista'),
    path('detalle/<int:pk>/', views.detalle_clientemayorista, name='detalle_cliente_mayorista'),
]