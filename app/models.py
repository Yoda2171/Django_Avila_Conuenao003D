from pickle import TRUE
from django.db import models

# Create your models here.


class Especie(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name="Id especie")
    nombreEspecie = models.CharField(max_length=69, verbose_name="nombre de la especie")

    def __str__(self):
        return self.nombreCategoria



class Mascota(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="id de la mascota")
    nombreMascota = models.CharField(max_length=50,verbose_name="Nombre de la mascota")
    nombreEspecie = models.ForeignKey(Especie,on_delete=models.CASCADE,verbose_name="Especie")
    raza = models.CharField(max_length=50,verbose_name="Raza")
    edad= models.IntegerField(verbose_name="edad")  
    nombreDueño = models.CharField(max_length=50,verbose_name="Nombre del dueño")

    def __str__(self):
        return self.nombreMascota

