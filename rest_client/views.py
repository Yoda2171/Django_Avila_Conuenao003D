from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Cliente 
from .serializers import ClienteSerializer
# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST','DELETE'])
def lista_cliente(request):

    if request.method=='GET':
        cliente = Cliente.objects.all()
        serializer =ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    if request.method=='POST':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['DELETE'])
def eliminarREST(request,id):
    if request.method=='DELETE':
        cliente= Cliente.objects.get(id_cliente=id)
        serializer =ClienteSerializer(cliente)
        cliente.delete()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
    else:
        return Response (status=status.HTTP_404_NOT_FOUND)



