from django.forms import modelform_factory

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.models import Persona
from personas.models import Domicilio


def detallePersona(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})


PersonaForm = modelform_factory(Persona, exclude=[])


def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def borrarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    persona.delete()
    return redirect('index')


# Funcion para crear, ver detalles, editar y borrar el domicilio
def detalleDomicilio(request, id):
    domicilio = Domicilio.objects.get(pk=id)
    return render(request, 'domicilios/detalle_domicilio.html', {'domicilio': domicilio})


DomicilioForm = modelform_factory(Domicilio, exclude=[])


def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm()
    return render(request, 'domicilios/nuevo_domicilio.html', {'formaDomicilio': formaDomicilio})


def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)
    return render(request, 'domicilios/editar_domicilio.html', {'formaDomicilio': formaDomicilio})


def borrarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    domicilio.delete()
    return redirect('index')
