from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.forms import modelform_factory, ModelForm, ValidationError
from finca.models import Finca, Cita
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from finca import forms as form


# Create your views here.

FincaForm = modelform_factory(Finca, exclude=[])


def nuevaFinca(request):
    print(request.POST)  # Imprime los datos enviados en la solicitud
    if request.method == 'POST':
        formaFinca = FincaForm(request.POST)
        print(formaFinca.is_valid())  # Imprime si el formulario es válido
        print(formaFinca.errors)
        if formaFinca.is_valid():
            formaFinca.save()
            return redirect('index')
    else:
        formaFinca = FincaForm()
    return render(request, 'admin/view_admin.html', {'formaFinca': formaFinca})


def editarFinca(request, id):
    print(request.POST)  # Imprime los datos enviados en la solicitud
    finca = get_object_or_404(Finca, pk=id)
    if request.method == 'POST':
        formaFinca = FincaForm(request.POST, instance=finca)
        print(formaFinca.is_valid())  # Imprime si el formulario es válido
        print(formaFinca.errors)
        if formaFinca.is_valid():
            formaFinca.save()
            return redirect('index')
    else:
        formaFinca = FincaForm(instance=finca)
    return render(request, 'admin/view_admin.html', {'formaFinca': formaFinca, 'finca': finca})


def borrarFinca(request, id):
    finca = get_object_or_404(Finca, pk=id)
    finca.delete()
    return redirect('index')


class CitaForm(ModelForm):
    finca = forms.ModelChoiceField(queryset=Finca.objects.all(), required=True)

    def clean_finca(self):
        finca = self.cleaned_data['finca']
        if not finca:
            raise ValidationError('Por favor, seleccione una finca.')
        return finca

    class Meta:
        model = Cita
        fields = '__all__'

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fecha_cita = request.POST['fecha_cita']

    def clean(self):
        cleaned_data = super().clean()
        finca = cleaned_data.get('finca')
        if finca is None:
            raise forms.ValidationError("Please select a finca.")
        return cleaned_data


def nuevaCita(request):
    finca_id = request.POST['finca_id']
    print('finca_id:', finca_id)
    finca = Finca.objects.get(pk=finca_id)
    print('finca:', finca)
    cita = Cita(
        nombre=request.POST['nombre'],
        apellido=request.POST['apellido'],
        email=request.POST['email'],
        fecha_cita=request.POST['fecha_cita'],
        finca=finca,
    )
    cita.save()
    return redirect('citas')


def borrarCita(request, id):
    cita = get_object_or_404(Finca, pk=id)
    cita.delete()
    return redirect('citas')


def Login(request):
    """
  Handles the login view.

  POST:
    Handles the login form submission.

  GET:
    Returns the login page.
  """
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username and password are valid
        user = authenticate(request, username=username, password=password)

        # If the user is valid, log them in
        if user is not None:
            Login(request, user)
            return redirect('admin/view_admin.html')
        else:
            # The username and password are not valid, so show an error message
            error_message = 'Invalid username or password.'
            return render(request, 'register.html', {'error_message': error_message})
    else:
        # The request is a GET, so return the login page
        return render(request, 'index.html')


class RoleOneSignUp(CreateView):
    form_class = form.RoleOneCreateForm
    success_url = reverse_lazy("accounts:role1_login")
    template_name = "accounts/role1/signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'role_one'
        return super().get_context_data(**kwargs)


class RoleTwoSignUp(CreateView):
    form_class = form.RoleTwoCreateForm
    success_url = reverse_lazy("accounts:role2_login")
    template_name = "accounts/role2/signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'role_two'
        return super().get_context_data(**kwargs)


