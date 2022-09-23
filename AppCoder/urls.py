from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('', inicio, name = "Inicio"),
    path("formularioEquipo/", formulario1, name = "formularioEquipo"),
    path("formularioJugador/", formulario2, name = "formularioJugador"),
    path("formularioEstadio/", formulario3, name = "formularioEstadio"),
    path("busqueda/", busqueda, name="Buscar"),
    path("busquedaEquipo/", busquedaEquipo, name="BuscarEquipo"),
    path("busquedaEstadio/", busquedaEstadio, name="BuscarEstadio"),
    path("buscar/", buscar),
    path("buscarEquipo/", buscarEquipo),
    path("buscarEstadio/", buscarEstadio),
]
 
   