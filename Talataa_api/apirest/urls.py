from django.urls import path
from .views import PedidoView, ConductorView

urlpatterns = [
    path('pedidos/', PedidoView.as_view(), name='pedidos_list'),
    path('pedidos/<int:id>', PedidoView.as_view(), name='pedidos_process'),
    path('conductores/', ConductorView.as_view(), name='conductores_list'),
    path('conductores/<int:id>', ConductorView.as_view(),
         name='conductores_process')
]
