from rest_framework import serializers
from app.models import Cliente 

class ClienteSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Cliente 
        fields =['id_cliente','nombre','email', 'telefono','direccion']