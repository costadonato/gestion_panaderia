from django.urls import path
from django.views.generic import TemplateView

from apps.informe import views

app_name = 'informe'
urlpatterns = [
    path('',TemplateView.as_view(template_name='informe/home_informes.html') , name='informes'),
    path('ventas/filtradas', views.informe_ventas_filtradas, name='informe_ventas_filtradas'),
    path('ventas', views.informe_ventas, name='informe_ventas'),
    path('prod_faltantes', views.informe_productos_faltantes, name='prod_faltantes'),
    path('matprima_faltante', views.informe_matprima_faltante, name='matprima_faltante'),
    path('productos_mas_vendidos', views.informe_productos_mas_vendidos, name='productos_mas_vendidos'),
    path('vendedores_mas_ventas',views.informe_empleados_mas_ventas, name='vendedores_mas_ventas' )
]