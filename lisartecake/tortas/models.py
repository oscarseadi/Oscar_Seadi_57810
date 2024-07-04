from django.db import models

# Productos LisArteCake
class Torta(models.Model):
    tipo = models.CharField(max_length=100)
    cubierta = models.CharField(max_length=200)
    relleno = models.CharField(max_length=250)
    cantidad_personas = models.IntegerField()

class TortaP(models.Model):
    tipo = models.CharField(max_length=100)
    cubierta = models.CharField(max_length=200)
    relleno = models.CharField(max_length=250)
    cantidad_personas = models.IntegerField()
    motivo = models.CharField(max_length=100)
    agregados = models.IntegerField()

class Modelado(models.Model):
    descripcion = models.CharField(max_length=250)
    dimensiones = models.CharField(max_length=50)
    misc = models.CharField(max_length=250)