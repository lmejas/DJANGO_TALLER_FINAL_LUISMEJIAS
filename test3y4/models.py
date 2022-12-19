from django.db import models
from unittest.util import _MAX_LENGTH
from .choices import choices

# Create your models here.

class Institucion(models.Model):
    institucion = models.CharField(max_length=50)
    def __str__(self):
        return self.institucion

class Seminario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fechaInscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    horaInscripcion = models.TimeField()
    estados = models.CharField(max_length=50, choices = choices)
    observacion = models.CharField(max_length=50, blank=True)

    