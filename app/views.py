from django.shortcuts import redirect, render

from app.models import Especie, Mascota

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

def mascotas(request):
    especie = Especie.objects.all()
    return render(request, "mascota.html", {"especie": especie})

def añadirMascota(request):
    mascota= Mascota()
    mascota.nombreMascota=request.POST["nombre_Mascota"]
    mascota.nombreEspecie=Especie.objects.get(nombreEspecie=request.POST["nombre_Especie"])
    mascota.raza=request.POST["raza_Mascota"]
    mascota.edad=request.POST["edad_mascota"]
    mascota.nombreDueño=request.POST["nombre_Dueño"]

    mascota.save()
   
 
    return redirect('galeria')

