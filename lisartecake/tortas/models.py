from django.db import models
from django.contrib.auth.models import User
from .models import *
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Productos LisArteCake
class Torta(models.Model):
    tipo = models.CharField(max_length=100)
    cubierta = models.CharField(max_length=200)
    relleno = models.CharField(max_length=250)
    cantidad_personas = models.IntegerField()
    precio = models.DecimalField(default=5000, max_digits=10, decimal_places=3)

    def __str__(self):
        return f"{self.tipo}, {self.cantidad_personas} personas"
    

class TortaP(models.Model):
    tipo = models.CharField(max_length=100)
    cubierta = models.CharField(max_length=200)
    relleno = models.CharField(max_length=250)
    cantidad_personas = models.IntegerField()
    motivo = models.CharField(max_length=100)
    agregados = models.CharField(max_length=50)
    precio = models.DecimalField(default=5000, max_digits=10, decimal_places=3)

    def __str__(self):
        return f"{self.tipo} , {self.motivo}, {self.cantidad_personas} personas"
    

class Modelado(models.Model):
    descripcion = models.CharField(max_length=250)
    dimensiones = models.CharField(max_length=50)
    misc = models.CharField(max_length=250)
    precio = models.DecimalField(default=5000, max_digits=10, decimal_places=3)

    def __str__(self):
        return f"{self.descripcion} - {self.dimensiones}"

class Cupcake(models.Model):
    tipo = models.CharField(max_length=100)
    cubierta = models.CharField(max_length=200)
    relleno = models.CharField(max_length=250)
    docenas = models.CharField(max_length=1)
    precio = models.DecimalField(default=5000, max_digits=10, decimal_places=3)
    
    def __str__(self):
        return f"{self.tipo}, {self.docenas} docenas"
    


    
#__Carrito
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Torta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.PositiveIntegerField(default=5000)

    def __str__(self):
        return f'{self.cantidad} de {self.producto.tipo}'
    
    

#__ Avatar

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.imagen}'


