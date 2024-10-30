from django.urls import path
from django.views.generic import TemplateView

from apps.informe import views

app_name = 'informe'
urlpatterns = [
    path('',TemplateView.as_view(template_name='informe/home_informes.html') , name='informes'),
    path('ventas/filtradas', views.informe_ventas_filtradas, name='informe_ventas_filtradas'),
    path('ventas', views.informe_ventas, name='informe_ventas'),
    path('prod_faltantes', views.informe_productos_faltantes, name='prod_faltantes')
]