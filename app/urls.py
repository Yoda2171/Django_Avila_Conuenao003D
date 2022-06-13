from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('somos/', views.somos,name="somos"),
    path('galeria/', views.galeria,name="galeria"),
    path('clientes/', views.clientes,name="clientes"),
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),
    path('contacto/', views.contacto,name="contacto"),
    path('mascota/',views.mascotas,name="mascota"),
    path('mascota/new/',views.añadirMascota,name="añadirMascota"),
    path('galeria/<id>/',views.eliminarMascota,name="eliminarMascota"),
    path('mascota/<id>/',views.editarMascota,name="editarMascota"),
    path('contacto/', views.contacto,name="contacto"),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
