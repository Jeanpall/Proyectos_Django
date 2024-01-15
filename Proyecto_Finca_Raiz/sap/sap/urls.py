"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp.views import bienvenido, login, register, administrador, usuario, sesionAdmin
from finca.views import nuevaFinca, editarFinca, borrarFinca

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path('', bienvenido, name='bienvenido'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('vista/', sesionAdmin, name='vistaAdmin'),
    path('administrador/', administrador, name='index'),
    path('usuario/', usuario, name='usuario'),
    path('nuevaFinca/', nuevaFinca, name='nuevaFinca'),
    path('editarFinca/<int:id>', editarFinca, name='editarFinca'),
    path('administrador/borrarfinca/<int:id>', borrarFinca),

]
