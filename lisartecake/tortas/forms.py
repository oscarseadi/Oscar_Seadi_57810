from django import forms 

class TortaForm(forms.Form):
    tipo = forms.CharField(max_length=100, required=True, label= "Elige un sabor")
    cubierta = forms.CharField(max_length=200, required=True, label= "Deseas cubierta?")
    relleno = forms.CharField(max_length=250, required=True, label= "Deseas relleno?")
    cantidad_de_personas = forms.IntegerField(required=True, label= "Para cuantas personas?")

class TortapForm(forms.Form):
    tipo =  forms.CharField(max_length=100, required=True, label= "Elige un sabor")
    cubierta = forms.CharField(max_length=200, required=True, label= "Deseas cubierta?")
    relleno = forms.CharField(max_length=250, required=True, label= "Deseas relleno?")
    cantidad_de_personas = forms.IntegerField(required=True, label= "Para cuantas personas?")
    motivo = forms.CharField(max_length=100, required=True, label= "Elige un motivo o tematica")
    agregado = forms.CharField(max_length=100, required=True, label="Incluye algún agregado o tope?")

class ModeladoForm(forms.Form):
    descripcion =  forms.CharField(max_length=100, required=True, label= "Describe el modelo")
    dimensiones = forms.CharField(max_length=200, required=True, label= "Especifica dimensiones")
    misc = forms.CharField(max_length=250, required=True, label= "Misceláneos")
    