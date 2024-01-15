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

from finca import views, forms
from webapp.views import bienvenido, login, register, administrador, usuario, sesionAdmin, citas
from finca.views import nuevaFinca, editarFinca, borrarFinca, borrarCita, nuevaCita, Login
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path('', bienvenido, name='bienvenido'),
    path('register/', register, name='register'),

    path('vista/', sesionAdmin, name='vistaAdmin'),
    path('administrador/', administrador, name='index'),
    path('nuevaFinca/', nuevaFinca, name='nuevaFinca'),
    path('editarFinca/<int:id>', editarFinca, name='editarFinca'),
    path('administrador/borrarfinca/<int:id>', borrarFinca),

    path('usuario/', usuario, name='usuario'),
    path('citas/', citas, name='citas'),
    path('nuevaCita/', nuevaCita, name='nuevaCita'),
    path('citas/borrarcita/<int:id>', borrarCita),

    path(r"^role1login/$", auth_views.LoginView.as_view(template_name="accounts/role1/login.html",
        extra_context={'next': '#',},redirect_authenticated_user=True,authentication_form=forms.RoleOneLogin),
        name='role1_login'),
    path(r"^role1logout/$", auth_views.LogoutView.as_view(), name="role1_logout"),
    path(r"^role1signup/$", views.RoleOneSignUp.as_view(), name="role1_signup"),
    path(r"^role2login/$", auth_views.LoginView.as_view(template_name="accounts/role2/login.html",redirect_authenticated_user=True,authentication_form=forms.RoleTwoLogin),name='role2_login'),
    path(r"^role2logout/$", auth_views.LogoutView.as_view(), name="role2_logout"),
    path(r"^role2signup/$", views.RoleTwoSignUp.as_view(), name="role2_signup"),
]
