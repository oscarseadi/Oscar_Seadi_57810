from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
    agregados = forms.CharField(max_length=100, required=True, label="Incluye algún agregado o tope?")

class ModeladoForm(forms.Form):
    descripcion =  forms.CharField(max_length=100, required=True, label= "Describe el modelo")
    dimensiones = forms.CharField(max_length=200, required=True, label= "Especifica dimensiones")
    misc = forms.CharField(max_length=250, required=True, label= "Misceláneos")
    

class RegistroFrom(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label="Nombre")
    last_name = forms.CharField(max_length=100, required=True, label="Apellido")
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email","username", "password1", "password2"]


class UserEditForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, required=True, label="Nombre")
    last_name = forms.CharField(max_length=100, required=True, label="Apellido")
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ["first_name", "last_name", "email","username"]

#___________________________________


#______________________________________

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)