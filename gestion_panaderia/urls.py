"""
URL configuration for gestion_panaderia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/', include('apps.producto.urls', namespace='producto')),
    path('ventas/', include('apps.venta.urls', namespace='venta')),
    path('materiaprima/', include('apps.pedido.urls', namespace='pedido')),
    path('proveedor/', include('apps.proveedor.urls', namespace='proveedor')),
    path('informes/', include('apps.informe.urls', namespace='informe')),
    path('cliente-mayorista/', include('apps.cliente_mayorista.urls', namespace='cliente_mayorista')),
    path('empleados/', include('apps.empleado.urls', namespace='empleado')),
    path('', include('apps.usuario.urls', namespace='usuario')),
    path('', views.home, name='home')
    #path('', TemplateView.as_view(template_name='base/home.html'), name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
