"""Talataa_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from apirest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # rutas peticiones
    path('apirest/', include('apirest.urls')),
    # rutas proyectos
    path('', views.home, name='home'),
    # rutas pedido
    path('pedido/', views.pedido, name='pedido'),
    path('pedido/crear/', views.createPedido, name='createPedido'),
    path('pedido/<int:pedido_id>/', views.detallePedido, name='detallePedido'),
    path('pedido/<int:pedido_id>/eliminar',
         views.eliminarPedido, name='eliminarPedido'),
    # rutas conductor
    path('conductor/', views.conductor, name='conductor'),
    path('conductor/<int:conductor_id>',
         views.detalleConductor, name='detalleConductor')
]
