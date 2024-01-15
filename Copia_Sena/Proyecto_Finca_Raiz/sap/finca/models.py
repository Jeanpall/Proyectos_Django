from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import auth


class Finca(models.Model):
    inmueble = models.CharField(max_length=255)
    precio = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    fecha = models.DateField()
    descripcion = models.TextField()
    imagen = models.URLField()

    def __str__(self):
        return f'Finca {self.id}:{self.inmueble}{self.precio}{self.direccion}'


class Cita(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    fecha_cita = models.DateField()
    finca = models.ForeignKey(Finca, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Cita de {self.nombre} {self.apellido}'


class User(auth.models.AbstractUser):
    is_role1 = models.BooleanField(default=False)
    is_role2 = models.BooleanField(default=False)

    # Agrega los atributos related_name con nombres únicos para evitar conflictos
    groups = models.ManyToManyField(Group, blank=True, related_name='user_set_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_set_user_permissions')

    def __str__(self):
        return "@{}".format(self.username)



