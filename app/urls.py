from django.contrib import admin
from django.urls import path
from django.views import View
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
]