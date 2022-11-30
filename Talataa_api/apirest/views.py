from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Pedido, Conductor
from .forms import PedidoForm
import json
import random

# Create your views here.

# Vista de peticiones de Pedidido


class PedidoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            Pedidos = list(Pedido.objects.filter(id=id).values())
            if len(Pedidos) > 0:
                pedido = Pedidos[0]
                datos = {'message': "Success", 'Pedidos': pedido}
            else:
                datos = {'message': "Not Success"}
            return JsonResponse(datos)
        else:
            Pedidos = list(Pedido.objects.values())
            if len(Pedidos) > 0:
                datos = {'message': "Success", 'Pedidos': Pedidos}
            else:
                datos = {'message': "Not Success"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        c = random.choice(Conductor.objects.values().filter(estado=1))
        Pedido.objects.create(nombre=jd['nombre'],
                              apellido=jd['apellido'],
                              correo=jd['correo'],
                              telefono=jd['telefono'],
                              direccion=jd['direccion'],
                              fecha_entrega=jd['fecha_entrega'],
                              franja_hora=jd['franja_hora'],
                              conductor=c['id'])
        Pedido.save()
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        Pedidos = list(Pedido.objects.filter(id=id).values())
        if len(Pedidos) > 0:
            pedido = Pedido.objects.get(id=id)
            pedido.nombre = jd['nombre']
            pedido.apellido = jd['apellido']
            pedido.correo = jd['correo']
            pedido.telefono = jd['telefono']
            pedido.direccion = jd['direccion']
            pedido.fecha_entrega = jd['fecha_entrega']
            pedido.franja_hora = jd['franja_hora']
            pedido.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Not Success"}
        return JsonResponse(datos)

    def delete(self, request, id):
        Pedidos = list(Pedido.objects.filter(id=id).values())
        if len(Pedidos) > 0:
            Pedido.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Not Success"}
        return JsonResponse(datos)

# Vista de peticion de Conductor


class ConductorView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            Conductores = list(Conductor.objects.filter(id=id).values())
            pedidos = list(Pedido.objects.filter(conductor=id).values())
            if len(Conductores) > 0:
                conductor = Conductores[0]
                datos = {'message': "Success",
                         'Conductores': conductor, 'Pedidos': pedidos}
            else:
                datos = {'message': "Not Success"}
            return JsonResponse(datos)
        else:
            Conductores = list(Conductor.objects.values())
            if len(Conductores) > 0:
                datos = {'message': "Success", 'Pedidos': Conductores}
            else:
                datos = {'message': "Not Success"}
            return JsonResponse(datos)

# Vista de los proyectos


def home(request):
    return render(request, 'home.html')

# vistas pedido


def pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido.html', {'pedidos': pedidos})


def detallePedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'GET':
        form = PedidoForm(instance=pedido)
        return render(request, 'detallePedido.html', {'pedido': pedido, 'form': form})
    else:
        form = PedidoForm(request.POST, instance=pedido)
        form.save()
        return redirect('pedido')


def eliminarPedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedido')


def createPedido(request):
    if request.method == 'GET':
        return render(request, 'createPedido.html', {
            'form': PedidoForm
        })
    elif request.method == 'POST':
        try:
            form = PedidoForm(request.POST)
            nuevo_pedido = form.save(commit=False)
            c = random.choice(Conductor.objects.values().filter(estado=1))
            nuevo_pedido.conductor = c['id']
            if nuevo_pedido.franja_hora > 0 and nuevo_pedido.franja_hora < 9:
                nuevo_pedido.save()
                return redirect('pedido')
            else:
                return render(request, 'createPedido.html', {
                    'form': PedidoForm,
                    'error': 'No se puede crear mayor de 8h'
                })
        except:
            return render(request, 'createPedido.html', {
                'form': PedidoForm,
                'error': 'Datos erroneos, por favor volverlo a digitar'
            })


def conductor(request):
    conductores = Conductor.objects.all()
    return render(request, 'conductor.html', {'conductores': conductores})


def detalleConductor(request, conductor_id):
    conductor = get_object_or_404(Conductor, pk=conductor_id)
    pedidos = Pedido.objects.filter(conductor=conductor_id)
    return render(request, 'detalleConductor.html', {'conductor': conductor, 'pedidos': pedidos})
