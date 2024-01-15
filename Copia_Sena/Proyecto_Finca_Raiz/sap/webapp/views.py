from django.http import HttpResponse
from django.shortcuts import render, redirect

from finca import forms
from finca.models import Finca, Cita, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView



# Create your views here.
def bienvenido(request):
    no_finca_var = Finca.objects.count()
    fincas = Finca.objects.all()
    return render(request, 'index.html',
                  {'no_finca': no_finca_var, 'fincas': fincas})


def login(request):
    no_user_var = User.objects.count()
    users = User.objects.all()
    return render(request, 'registration/login.html',
                  {'no_user': no_user_var, 'users': users})


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
    citas = Cita.objects.all()
    for cita in citas:
        print('cita.finca:', cita.finca)
    return render(request, 'admin/agendarCita.html',
                  {'no_cita': no_cita_var, 'citas': citas})


def usuario(request):
    fincas = Finca.objects.all()
    return render(request, 'view_user.html',
                  {'fincas': fincas})






