from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.forms import modelform_factory
from finca.models import Finca
from django.shortcuts import render, get_object_or_404, redirect

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


def login(request):
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
      login(request, user)
      return redirect('vistaAdmin')
    else:
      # The username and password are not valid, so show an error message
      error_message = 'Invalid username or password.'
      return render(request, 'login.html', {'error_message': error_message})
  else:
    # The request is a GET, so return the login page
    return render(request, 'login.html')
