from django.db import models


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

    def __str__(self):
        return f'Domicilio {self.id}:{self.nombre} {self.apellido} {self.email}'


class User(models.Model):
    """
  A model for users.

  Args:
    username: The username of the user.
    password: The password of the user.
    email: The email address of the user.
  """

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    admin = models.BooleanField(default=False)
    email = models.EmailField()

