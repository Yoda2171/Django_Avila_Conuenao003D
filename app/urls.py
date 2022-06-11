from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('somos/', views.somos,name="somos"),
    path('galeria/', views.galeria,name="galeria"),
    path('clientes/', views.clientes,name="clientes"),
    path('register/', views.register,name="register"),
    path('contacto/', views.contacto,name="contacto"),
    path('accounts/', include('django.contrib.auth.urls')),
]