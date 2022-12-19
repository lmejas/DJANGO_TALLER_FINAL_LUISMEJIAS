from django.shortcuts import render, redirect
from test3y4.models import Seminario, Institucion
from test3y4.forms import FormSeminario
from django.http import JsonResponse
from .serializers import SeminarioSerializer, InstitucionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404


def index(request):
    return render(request, 'index.html')

def listarinscripcion(request):
    sem = Seminario.objects.all()
    data = {'Seminario': sem}
    return render(request, 'listado.html', data)

def agregarindividuo(request):
    form = FormSeminario()
    if request.method == 'POST':
        form = FormSeminario(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarindividuo.html', data)

def eliminarinscripcion(request, id):
    sem = Seminario.objects.get(id = id)
    sem.delete()
    return redirect('/inscripciones')

def actualizarinscripcion(request, id):
    sem = Seminario.objects.get(id = id)
    form = FormSeminario(instance=sem)
    if request.method == 'POST':
        form = FormSeminario(request.POST, instance=sem)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarindividuo.html', data)

#API

def listarAPI(request):
    inscritos = Seminario.objects.all()
    data = {'inscritos' : list(inscritos.values('id', 'nombre', 'telefono', 'fechaInscripcion', 'institucion', 'horaInscripcion', 'estados', 'observacion'))}

    return JsonResponse(data)

#CLASS BASED VIEW

class inscritosLista(APIView):

    def get(self, request):
        estu = Seminario.objects.all()
        serial = SeminarioSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = SeminarioSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class inscritosDetalles(APIView):

    def get_object(self, pk):
        try:
            return Seminario.objects.get(pk=pk)
        except Seminario.DoesNotExist:
            return Http404

    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = SeminarioSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = SeminarioSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#FUNCTION BASED VIEW

@api_view(['GET', 'POST'])
def listadeinscritos(request):
    if request.method == 'GET':
        estu = Institucion.objects.all()
        serial = InstitucionSerializer(estu, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalledeinscritos(request, pk):
    try:
        estu = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionSerializer(estu)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)