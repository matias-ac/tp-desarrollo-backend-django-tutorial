from django.db import models
from alumno.models import Alumno
from profesor.models import Profesor

# Create your models here.

class Cursada(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    alumnos = models.ManyToManyField(Alumno, related_name="cursadas")
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cursada {self.fecha_inicio} - {self.fecha_fin} con {self.profesor}"
