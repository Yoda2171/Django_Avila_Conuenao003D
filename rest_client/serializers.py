from rest_framework import serializers
from app.models import Cliente 

class ClienteSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Cliente 
        fields =['nombre','email', 'telefono','direccion']