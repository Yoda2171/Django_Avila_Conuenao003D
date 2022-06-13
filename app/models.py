
from django.db import models
import datetime
import os

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
    id = models.BigAutoField(primary_key=True,verbose_name="Id mascota")
    nombreMascota = models.CharField(max_length=50,verbose_name="Nombre de la mascota")
    nombreEspecie = models.ForeignKey(Especie,on_delete=models.CASCADE,verbose_name="Especie")
    raza = models.CharField(max_length=50,verbose_name="Raza")
    edad= models.IntegerField(verbose_name="edad")  
    nombreDueño = models.CharField(max_length=50,verbose_name="Nombre del dueño")
    imagenMascota= models.ImageField(upload_to=filepath,verbose_name="imagen de la mascota")

    def __str__(self):
        return self.nombreMascota

