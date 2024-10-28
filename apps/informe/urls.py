from django.urls import path
from django.views.generic import TemplateView

from apps.producto import views

app_name = 'informe'
urlpatterns = [
    path('',TemplateView.as_view(template_name='informe/home_informes.html') , name='informes')
]