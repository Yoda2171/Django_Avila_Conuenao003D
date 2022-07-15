from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from app.models import Cliente, Especie, Mascota, CarritoCliente,CompraRealizada


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
            if (request.user.is_superuser):
                user = User.objects.all()
                return render(request,"carrito.html",{"clientes":user})

            else:
                carrito=CarritoCliente.objects.filter(id_user=request.user.id)
                carro=list(map(lambda x: x.id_mascota, carrito))

                if (len( carro ) != 0):
                    return render(request,"carrito.html",{"carrito":carro})
                else:
                    return render(request,"carrito.html")


def equipo(request):
    return render(request,"equipo.html")

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
        if(request.user.is_superuser == True):
            return render(request, "mascota.html", {"especie": especie})
        else:
            return redirect('index')

def añadirMascota(request):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        if(request.user.is_superuser == True):
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
        else:
            return redirect('index')
            

def eliminarMascota(request,id):
    if(not request.user.is_authenticated):
        return redirect('login')
        
    else:
        if(request.user.is_superuser == True):
            mascota= Mascota.objects.get(id_mascota=id)
            mascota.delete()
            return redirect('galeria')
        else:
            return redirect('index')


def editarMascota(request,id):
    data = {
        
        "especies" : Especie.objects.all(),
        "mascota": Mascota.objects.get(id_mascota=id),
    
    }

    if(not request.user.is_authenticated):
        return redirect('login')

    else:
        if(request.user.is_superuser == True):
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
        else:
            return redirect('index')
   
def cliente(request):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        if(request.user.is_superuser == True):
            cliente=Cliente.objects.all()
            return render(request,"cliente.html",{"cliente":cliente})
        else:
            return redirect('index')

def añadirCliente(request):

        if request.method == 'POST':

            cliente= Cliente()
            cliente.nombre=request.POST.get("nombre_cliente")
            cliente.email=request.POST.get("email_cliente")
            cliente.direccion=request.POST.get("direccion_cliente")
            cliente.telefono=request.POST.get("telefono_cliente")
            cliente.password=request.POST.get("contraseña_cliente")
            cliente.save()

            if cliente.password == request.POST.get("contraseña_cliente2"):
                if User.objects.filter(email=cliente.email).exists():
                    return render(request,"register.html",{"error":"El correo ya existe"})
                else:
                    user = User.objects.create_user(username=cliente.nombre, password=cliente.password,email=cliente.email)
                    user.save();

            return redirect('cliente')
            

def eliminarCliente(request,id):
    
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        if(request.user.is_superuser == True):
            cliente= Cliente.objects.get(id_cliente=id)
            cliente.delete()
            return redirect('cliente')
        else:
            return redirect('index')


def editarCliente(request,id):
    cliente= Cliente.objects.get(id_cliente=id)
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        if(request.user.is_superuser == True):
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
        else:
            return redirect('index')



def carro(request,id):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        mascota = Mascota.objects.get(id_mascota=id)
        carrito=CarritoCliente.objects.filter(id_user=request.user.id)
        carro=list(map(lambda x: x.id_mascota, carrito))


        if mascota in carro:
            print("ya esta en el carrito")
            return redirect('galeria') 
        else:
            carrito=CarritoCliente()
            carrito.id_user=User.objects.get(id=request.user.id)
            carrito.id_mascota=mascota
            carrito.save()
            
            print("agregado")
            return redirect('galeria') 

def carro_eliminar(request,id):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        
        carrito=CarritoCliente.objects.get(id_user=request.user.id,id_mascota=id)
        carrito.delete()
        

        return redirect('carrito')


        
def lista_carrito(request,id):
    if(not request.user.is_authenticated):
        return redirect('login')
    else:
        carrito=CarritoCliente.objects.filter(id_user=id)
        carro=list(map(lambda x: x.id_mascota, carrito))

        if (len( carro ) != 0):
                return render(request,"listaCarrito.html",{"carrito":carro})
        else:
            return render(request,"carrito.html")
      
    