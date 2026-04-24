from django.shortcuts import render
from .models import Alumno

# Create your views here.

def lista_alumnos(request):
    alumnos = Alumno.objects.all()

    return render(request, 'alumno/lista_alumnos.html', {'alumnos': alumnos})
