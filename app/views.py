
from re import U
from site import USER_BASE
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from app.models import Especie, Mascota


# Create your views here.
def index(request):
    return render(request,"index.html")

def somos(request):
    return render(request,"somos.html")

def galeria(request):
    mascotas = Mascota.objects.all()
    if(len(mascotas) != 0):
        return render(request,"galeria.html", {"mascotas": mascotas})
    else:
        return render(request,'galeria.html')
       

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
    if(not request.user.is_authenticated):
       return redirect('login')
    else:
        return render(request, "mascota.html", {"especie": especie})

def añadirMascota(request):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        if request.method == 'POST':

            mascota= Mascota()
            mascota.nombreMascota=request.POST.get("nombre_Mascota")
            mascota.nombreEspecie=Especie.objects.get(nombreEspecie=request.POST.get("nombre_Especie") )
            mascota.raza=request.POST.get("raza_Mascota")
            mascota.edad=request.POST.get("edad_mascota")
            mascota.nombreDueño=request.POST.get("nombre_Dueño")

            if len(request.FILES)!=0:
                mascota.imagenMascota=request.FILES["imagen_mascota"]

            mascota.save()
            return redirect('galeria')
            

def eliminarMascota(request,id):
    if(not request.user.is_authenticated):
        return redirect('login')
        
    else:
        mascota= Mascota.objects.get(id=id)
        mascota.delete()
        return redirect('galeria')


def editarMascota(request,id):
    data = {
        
        "especies" : Especie.objects.all(),
        "mascota": Mascota.objects.get(id=id),
    
    }

    if(not request.user.is_authenticated):
        return redirect('login')

    else:
        
        if request.method == 'POST':
            mascota= Mascota.objects.get(id=id)
            mascota.nombreMascota=request.POST.get("nombre_Mascota")

            if(mascota.nombreEspecie == mascota.nombreEspecie):
                mascota.nombreEspecie= Especie.objects.get(nombreEspecie=request.POST.get("nombre_Especie") )
            else:
                pass
            mascota.raza=request.POST.get("raza_Mascota")
            mascota.edad=request.POST.get("edad_mascota")
            mascota.nombreDueño=request.POST.get("nombre_Dueño")

            if len(request.FILES)!=0:
                mascota.imagenMascota=request.FILES["imagen_mascota"]
                
            mascota.save()
            return redirect('galeria')
        
        return render(request,"editMascota.html",data)
   

