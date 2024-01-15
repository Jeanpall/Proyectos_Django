from django.http import HttpResponse
from django.shortcuts import render
from finca.models import Finca, Cita


# Create your views here.
def bienvenido(request):
    no_finca_var = Finca.objects.count()
    fincas = Finca.objects.all()
    return render(request, 'index.html',
                  {'no_finca': no_finca_var, 'fincas': fincas})



def login(request):
    return render(request, 'registration/login.html')


def register(request):
    return render(request, 'register.html')


def administrador(request):
    no_finca_var = Finca.objects.count()
    fincas = Finca.objects.all()
    return render(request, 'admin/view_admin.html',
                  {'no_finca': no_finca_var, 'fincas': fincas})


def sesionAdmin(request):
    no_finca_var = Finca.objects.count()
    fincas = Finca.objects.all()
    return render(request, 'bienvenido_admin.html',
                  {'no_finca': no_finca_var, 'fincas': fincas})

def citas(request):
    no_cita_var = Cita.objects.count()
    cita = Cita.objects.all()
    return render(request, 'admin/agendarCita.html',
                  {'no_cita': no_cita_var, 'citas': cita})


def usuario(request):
    fincas = Finca.objects.all()
    return render(request, 'view_user.html',
                  {'fincas': fincas})
