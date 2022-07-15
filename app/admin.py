from django.contrib import admin
from .models import Especie,Mascota,Cliente,CarritoCliente

# Register your models here.
admin.site.register(Especie)
admin.site.register(Mascota)
admin.site.register(Cliente)
admin.site.register(CarritoCliente)