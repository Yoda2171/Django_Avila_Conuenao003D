from django.urls import path
from . import views


urlpatterns = [
    path('lista_cliente/',views.lista_cliente, name="lista_cliente"),
    path('lista_cliente/<id>/',views.eliminarREST,name="eliminarREST"),
]
