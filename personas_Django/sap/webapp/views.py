from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona
from personas.models import Domicilio


# Create your views here.

def bienvenido(request):
    no_domicilios_var = Domicilio.objects.count()
    no_personas_var = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    domicilios = Domicilio.objects.order_by('id')
    return render(request, 'bienvenido.html',
                  {'no_personas': no_personas_var, 'personas': personas,
                   'no_domicilios': no_domicilios_var, 'domicilios': domicilios})


def Despedida(request):
    return HttpResponse('Hasta la proxima')
