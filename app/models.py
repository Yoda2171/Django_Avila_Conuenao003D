from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=200,verbose_name="Nombre de la mascota")
    especie = models.CharField(max_length=200,verbose_name="Especie")
    raza = models.CharField(max_length=50,verbose_name="Raza")
    edad= models.IntegerField(verbose_name="Raza")

