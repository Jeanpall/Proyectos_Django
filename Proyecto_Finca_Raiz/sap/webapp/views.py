from django.http import HttpResponse
from django.shortcuts import render
from finca.models import Finca


# Create your views here.
def bienvenido(request):
    return render(request, 'index.html')


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
    return render(request, 'bienvenido_admin.html')


def usuario(request):
    return render(request, 'view_user.html')
