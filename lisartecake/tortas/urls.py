from django.urls import path, include
from.views import *

urlpatterns = [
    path('', home, name = "home"),
    path('home/', home, name = "home"),
    path('tortas/', tortas, name = "tortas"),
    path('tortasp/', tortasp, name = "tortasp"),
    path('modelados/', modelados, name = "modelados"),

    #__ Formularios

    path('tortas_form/', tortaForm, name = "tortaForm"),
    path('tortasp_form/', tortapForm, name = "tortapForm"),
    path('modelados_form/', modeladoForm, name = "modeladoForm"),

    path('buscarTorta/', buscarTorta, name = "buscarTorta"),
    path('encontrarTorta/', encontrarTorta, name = "encontrarTorta"),
]