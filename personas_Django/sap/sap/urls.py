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
from django.urls import path
from webapp.views import bienvenido
from personas.views import detallePersona
from personas.views import nuevaPersona
from personas.views import editarPersona
from personas.views import borrarPersona
from personas.views import detalleDomicilio
from personas.views import nuevoDomicilio
from personas.views import editarDomicilio
from personas.views import borrarDomicilio

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('bienvenido/', bienvenido),
    path('', bienvenido, name='index'),
    path('nueva_persona', nuevaPersona),
    path('detalle_persona/<int:id>', detallePersona),
    path('editar_persona/<int:id>', editarPersona),
    path('borrar_persona/<str:id>', borrarPersona),

    path('nuevo_domicilio', nuevoDomicilio),
    path('detalle_domicilio/<int:id>', detalleDomicilio),
    path('editar_domicilio/<int:id>', editarDomicilio),
    path('borrar_domicilio/<str:id>', borrarDomicilio),
]

