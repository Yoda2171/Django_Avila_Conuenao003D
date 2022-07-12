from ssl import SSLSession
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from app.models import Cliente, Especie, Mascota


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
       
def carrito(request):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        session=request.session.get('carro',{ "mascota": []})
        mascota=Mascota.objects.filter(id_mascota__in=session["mascota"])
        data={ "mascota": mascota }
    return render(request,"carrito.html", data)

def equipo(request):
    return render(request,"equipo.html")

def register(request):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
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
            mascota.precio=request.POST.get("precio_mascota")
            mascota.nombreDueño=request.POST.get("nombre_Dueño")

            if len(request.FILES)!=0:
                mascota.imagenMascota=request.FILES["imagen_mascota"]

            mascota.save()
            return redirect('galeria')
            

def eliminarMascota(request,id):
    if(not request.user.is_authenticated):
        return redirect('login')
        
    else:
        mascota= Mascota.objects.get(id_mascota=id)
        mascota.delete()
        return redirect('galeria')


def editarMascota(request,id):
    data = {
        
        "especies" : Especie.objects.all(),
        "mascota": Mascota.objects.get(id_mascota=id),
    
    }

    if(not request.user.is_authenticated):
        return redirect('login')

    else:
        if request.method == 'POST':
            mascota= Mascota.objects.get(id_mascota=id)
            mascota.nombreMascota=request.POST.get("nombre_Mascota")

            if(mascota.nombreEspecie == mascota.nombreEspecie):
                mascota.nombreEspecie= Especie.objects.get(nombreEspecie=request.POST.get("nombre_Especie") )
            else:
                pass
            mascota.raza=request.POST.get("raza_Mascota")
            mascota.precio=request.POST.get("precio_mascota")
            mascota.nombreDueño=request.POST.get("nombre_Dueño")

            if len(request.FILES)!=0:
                mascota.imagenMascota=request.FILES["imagen_mascota"]
                
            mascota.save()
            return redirect('galeria')
        
        return render(request,"editMascota.html",data)
   
def cliente(request):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        cliente=Cliente.objects.all()
        return render(request,"cliente.html",{"cliente":cliente})

def añadirCliente(request):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        if request.method == 'POST':

            cliente= Cliente()
            cliente.nombre=request.POST.get("nombre_cliente")
            cliente.email=request.POST.get("email_cliente")
            cliente.direccion=request.POST.get("direccion_cliente")
            cliente.telefono=request.POST.get("telefono_cliente")
            cliente.password=request.POST.get("contraseña_cliente")
        
            cliente.save()
            return redirect('cliente')
            

def eliminarCliente(request,id):
    if(not request.user.is_authenticated):
        return redirect('login')
        
    else:
        cliente= Cliente.objects.get(id_cliente=id)
        cliente.delete()
        return redirect('cliente')


def editarCliente(request,id):
    cliente= Cliente.objects.get(id_cliente=id)
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        if request.method == 'POST':
            
            cliente= Cliente.objects.get(id_cliente=id)
            cliente.nombre=request.POST.get("nombre_cliente")
            cliente.direccion=request.POST.get("direccion_cliente")
            cliente.telefono=request.POST.get("telefono_cliente")
            cliente.email=request.POST.get("email_cliente")
            cliente.password=request.POST.get("contraseña_cliente")
            
            cliente.save()

            return redirect('cliente')
        return render(request,"editCliente.html",{"cliente":cliente})    
        



def carro(request,id):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        mascota = Mascota.objects.get(id_mascota=id)
        initial ={ "mascota": [],"precio":0}
        session = request.session.get("carro", initial)
        if id in session["mascota"]:
            print("ya existe")
        else:
            session["mascota"].append(id)
            session["precio"]=(mascota.precio)
            request.session["carro"] = session
            print("agregado")
            print( session["mascota"])
        return redirect('carrito')

def carro_eliminar(request,id):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        session = request.session.get("carro", {})
        session["mascota"].remove(id)
        request.session["carro"] = session
        return redirect('carrito')


        
       
    