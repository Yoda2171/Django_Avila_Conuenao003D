from django.shortcuts import render

from app.models import Especie

# Create your views here.
def index(request):
    return render(request,"index.html")
def somos(request):
    return render(request,"somos.html")
def galeria(request):
    return render(request,"galeria.html")
def clientes(request):
    return render(request,"clientes.html")
def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")
def contacto(request):
    return render(request,"contacto.html")
def añadirmascota(request):
    especie = Especie.objects.all()
    return render(request, "mascota.html", {"especie": especie})

