from django.forms import ModelForm
from .models import Pedido, Conductor

# crear formulario de modelo pedido:


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre',
                  'apellido',
                  'correo',
                  'telefono',
                  'direccion',
                  'fecha_entrega',
                  'franja_hora']
