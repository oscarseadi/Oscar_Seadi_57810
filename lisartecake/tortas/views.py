from django.shortcuts import render
from.models import *

from.forms import *

def home(request):
    return render(request, "tortas/index.html")

#___ Torta

def tortas(request):
    contexto = {"tortas": Torta.objects.all()}
    return render(request, "tortas/tortas.html", contexto)

def tortaForm(request):
    if request.method == "POST":
        miForm = TortaForm(request.POST)
        if miForm.is_valid():
            torta_tipo = miForm.cleaned_data.get("tipo")
            torta_cubierta = miForm.cleaned_data.get("cubierta")
            torta_relleno = miForm.cleaned_data.get("relleno")
            torta_cantidad_de_personas = miForm.cleaned_data.get("cantidad_de_personas")
            torta = Torta(tipo=torta_tipo, cubierta=torta_cubierta, relleno=torta_relleno, cantidad_personas=torta_cantidad_de_personas)
            torta.save()
            contexto = {"tortas": Torta.objects.all() }
            return render(request, "tortas/tortas.html", contexto)
    else:
        miForm = TortaForm()

    return render(request, "tortas/tortaForm.html", {"form": miForm})

#__ Buscar

def buscarTorta(request):
    return render(request, "tortas/buscar.html")

def encontrarTorta(request):
    if request.GET["Buscar"]:
        patron = request.GET["Buscar"]
        torta = Torta.objects.filter(tipo__icontains=patron)
        contexto = {'tortas': torta}
    else:
        contexto = {"tortas": Torta.objects.all()} 

    return render(request, "tortas/tortas.html", contexto)



#___ Tortap

def tortasp(request):
    contexto = {"tortasp": TortaP.objects.all()}
    return render(request, "tortas/tortasp.html", contexto)

def tortapForm(request):
    if request.method == "POST":
        miForm = TortapForm(request.POST)
        if miForm.is_valid():
            torta_tipo = miForm.cleaned_data.get("tipo")
            torta_cubierta = miForm.cleaned_data.get("cubierta")
            torta_relleno = miForm.cleaned_data.get("relleno")
            torta_cantidad_de_personas = miForm.cleaned_data.get("cantidad_de_personas")
            torta_motivo = miForm.cleaned_data.get("motivo")
            torta_agregado = miForm.cleaned_data.get("agregado")
            torta = TortaP(tipo=torta_tipo, cubierta=torta_cubierta, relleno=torta_relleno, cantidad_personas=torta_cantidad_de_personas, motivo=torta_motivo, agregado=torta_agregado)
            torta.save()
            contexto = {"tortasp": TortaP.objects.all() }
            return render(request, "tortas/tortasp.html", contexto)
    else:
        miForm = TortapForm()

    return render(request, "tortas/tortapForm.html", {"form": miForm})

#___ Modelado

def modelados(request):
    contexto = {"modelados": Modelado.objects.all()}
    return render(request, "tortas/modelados.html", contexto)

def modeladoForm(request):
    if request.method == "POST":
        miForm = ModeladoForm(request.POST)
        if miForm.is_valid():
            modelo_descripcion = miForm.cleaned_data.get("descripcion")
            modelo_dimensiones = miForm.cleaned_data.get("dimensiones")
            modelo_miscelaneos = miForm.cleaned_data.get("miscelaneos")
            modelo = Modelado(descripcion=modelo_descripcion, dimensiones=modelo_dimensiones, misc=modelo_miscelaneos)
            modelo.save()
            contexto = {"modelados": Modelado.objects.all() }
            return render(request, "tortas/modelados.html", contexto)
    else:
        miForm = ModeladoForm()

    return render(request, "tortas/modeladoForm.html", {"form": miForm})