from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
]
