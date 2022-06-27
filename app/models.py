
from django.db import models
import datetime
import os

from django.forms import PasswordInput

# Create your models here.


class Especie(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name="Id especie")
    nombreEspecie = models.CharField(max_length=69, verbose_name="nombre de la especie")

    def __str__(self):
        return self.nombreEspecie


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('images/', filename) 

class Mascota(models.Model):
    id_mascota = models.BigAutoField(primary_key=True,verbose_name="Id mascota")
    nombreMascota = models.CharField(max_length=50,verbose_name="Nombre de la mascota")
    nombreEspecie = models.ForeignKey(Especie,on_delete=models.CASCADE,verbose_name="Especie")
    raza = models.CharField(max_length=50,verbose_name="Raza")
    precio= models.IntegerField(verbose_name="precio")  
    nombreDueño = models.CharField(max_length=50,verbose_name="Nombre del dueño")
    imagenMascota= models.ImageField(upload_to=filepath,verbose_name="imagen de la mascota")

    def __str__(self):
        return self.nombreMascota


class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True,verbose_name="Id cliente")
    nombre = models.CharField(max_length=50,verbose_name="Nombre del cliente")
    email=models.CharField(max_length=50,verbose_name="correo del cliente")
    direccion = models.CharField(max_length=50, verbose_name="dirrecion")
    telefono=models.IntegerField(verbose_name="telefono")
    password=models.CharField(max_length=50, verbose_name="contraseña")
    
    def __str__(self):
        return self.nombre


class CarritoCliente(models.Model):
    id_carrito = models.BigAutoField(primary_key=True,verbose_name="Id carrito")
    id_cliente = models.ForeignKey(Mascota,on_delete=models.CASCADE,verbose_name="Mascota")
    id_mascota = models.ForeignKey(Cliente,on_delete=models.CASCADE,verbose_name="Cliente")

    def __str__(self):
        return self.id_carrito
