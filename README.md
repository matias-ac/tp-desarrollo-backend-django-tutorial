# TP Nro 3 - Desarrollo de Sistemas Backend - Tutorial Django

## Paso 1: Crear un entorno virtual

Abre tu terminal.

Ejecuta el siguiente comando para crear un entorno virtual:

python -m venv Env

Activa el entorno virtual:

En Windows:

.\Env\Scripts\activate

En MacOS/Linux:

source Env/bin/activate

## Paso 2: Instalar Django

Con el entorno virtual activado, instala Django usando pip:

pip install django

## Paso 3: Crear el Proyecto Django

Crea un nuevo proyecto llamado Instituto con el siguiente comando:

django-admin startproject Instituto

Cambia al directorio del proyecto:
cd Instituto

Paso 4: Crear las Apps

Crea las aplicaciones alumno, profesor y cursada:

python manage.py startapp alumno
python manage.py startapp profesor
python manage.py startapp cursada

Paso 5: Configurar las Apps en el Proyecto

Abre el archivo Instituto/settings.py.

En el apartado INSTALLED_APPS, agrega las nuevas apps:

INSTALLED_APPS = [

Apps de Django por defecto

'django.contrib.admin',

'django.contrib.auth',

'django.contrib.contenttypes',

'django.contrib.sessions',

'django.contrib.messages',

'django.contrib.staticfiles',

Nuevas apps

'alumno',

'profesor',

'cursada',

]

Paso 6: Crear los Modelos

Modelo Alumno en alumno/models.py:

from django.db import models

class Alumno (models. Model):

nombre

models. CharField(max_length=100)

apellido models. CharField(max_length $=100$)

edad  models. IntegerField()

email

models. EmailField()

def str(self):

return f" {self.nombre} {self.apellido}"

Modelo Profesor en profesor/models.py:

from django.db import models

class Profesor (models. Model):

nombre models. CharField(max_length $=100$)
apellido models. CharField(max_length=100)
materia  models. CharField(max_length= $=100$)
email  models. EmailField()

def str(self):

return f" (self.nombre (self.apellido} {self.materia}"

Modelo Cursada en cursada/models.py:

from django.db import models

from alumno.models import Alumno

from profesor.models import Profesor

class Cursada (models. Model):

fecha_inicio  models. DateField()
fecha_fin  models. DateField()

alumnos  models. Many ToMany Field (Alumno,

related_name="cursadas")

profesor  models. ForeignKey (Profesor, on_delete=models.CASCADE)

def str(self):

return f"Cursada  self.fecha_inicio} {self.fecha_fin} con

{self.profesor}"

Paso 7: Configurar los Administradores

En cada archivo admin. py de las apps, registra los modelos para que sean visibles en el panel de administración.

alumno/admin.py:

from django.contrib import admin

from.models import Alumno

admin.site.register (Alumno)

profesor/admin.py:

from django.contrib import admin
from.models import Profesor

admin.site.register (Profesor)

cursada/admin.py:

from django.contrib import admin
from models import Cursada

admin.site.register (Cursada)

Paso 8: Migrar la Base de Datos

Crea las tablas en la base de datos ejecutando las migraciones:

python manage.py makemigrations
python manage.py migrate

Paso 9: Crear una Vista y Template

Vista basada en función: crea una vista en alumno/views.py que muestre una lista de alumnos.

from django.shortcuts import render

from.models import Alumno

def lista_alumnos (request):

alumnos Alumno.objects.all()

return render (request, 'alumno/lista_alumnos.html', {'alumnos':

alumnos})

Template básico: crea el archivo templates/alumno/lista_alumnos.html.

<!DOCTYPE html>

<html lang="es">

<head>

<meta charset="UTF-8">

<title>Lista de Alumnos</title>

</head>

<body>

<h1>Lista de Alumnos</h1>

<ul>

{% for alumno in alumnos %}

<li>{{ alumno.nombre }} {{ alumno.apellido }}</li>

{% endfor %}

</ul>

</body>

</html>


Configurar URL: en alumno/urls.py, agrega una ruta para la vista lista_alumnos.

from django.urls import path

from import views

urlpatterns = [

path('alumnos/', views.lista_alumnos, name='lista_alumnos'),

1

Incluir las URLs en el proyecto principal Instituto/urls.py:

from django.contrib import admin

from django.urls import path, include

urlpatterns $=[$

path('admin/', admin.site.urls),

path('', include('alumno.urls')),

]

Paso 10: Ejecutar el Servidor

Inicia el servidor y verifica la vista:

python manage.py runserver

Visita http://127.0.0.1:8000/alumnos/ en tu navegador para ver la lista de alumnos.
