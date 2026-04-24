from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.materia}"
