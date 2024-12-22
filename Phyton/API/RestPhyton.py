

                                                      Servicio Rest http


                                   esponer servicios http con phyton post, get, put, delete con django
¡Genial! Vamos a crear una API RESTful con Django que exponga servicios HTTP para operaciones POST, GET, PUT y DELETE. Utilizaremos el framework Django REST para facilitar el proceso.

Paso 1: Configurar el Entorno
Instalar Django y Django REST framework: Primero, necesitas instalar Django y Django REST framework. Puedes hacerlo desde la terminal usando pip:

bash
pip install django djangorestframework
Crear un Proyecto Django:

bash
django-admin startproject crud_project
cd crud_project
Crear una Aplicación Django:

bash
python manage.py startapp usuarios

----------------------------------------------------------------------------------------------------------------------------------
Paso 2: Configurar el Proyecto
Agregar las Aplicaciones al Proyecto: En crud_project/settings.py, añade 'rest_framework' y 'usuarios' a la lista de INSTALLED_APPS:

python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'usuarios',
]

----------------------------------------------------------------------------------------------------------------------------------
Paso 3: Crear el Modelo y Serializador
Definir el Modelo Usuario: En usuarios/models.py:

python
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
Crear el Serializador: En usuarios/serializers.py:

python
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
------------------------------------------------------------------------------------------------------------------------------------
Paso 4: Crear las Vistas
Crear las Vistas para el CRUD: En usuarios/views.py:

python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer

@api_view(['GET', 'POST'])
def usuario_lista(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detalle(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
-------------------------------------------------------------------------------------------------------------------------------------
Paso 5: Configurar las URLs
Configurar las URLs de la Aplicación: En usuarios/urls.py:

python
from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuario_lista),
    path('usuarios/<int:pk>/', views.usuario_detalle),
]
Incluir las URLs de la Aplicación en el Proyecto: En crud_project/urls.py:

python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('usuarios.urls')),
]


-------------------------------------------------------------------------------------------------------------------------------
Paso 6: Ejecutar el Proyecto
Aplicar Migraciones:

bash
python manage.py makemigrations
python manage.py migrate
Ejecutar el Servidor de Desarrollo:

bash
python manage.py runserver
Probar la API
Puedes probar tu API utilizando herramientas como curl o Postman.

Ejemplos de Uso con curl:
POST (Crear):

bash
curl -X POST http://127.0.0.1:8000/api/usuarios/ -H "Content-Type: application/json" -d '{"nombre":"Juan","apellido":"Pérez","email":"juan.perez@example.com","edad":28}'
GET (Leer todos los usuarios):

bash
curl http://127.0.0.1:8000/api/usuarios/
GET (Leer un usuario específico):

bash
curl http://127.0.0.1:8000/api/usuarios/1/
PUT (Actualizar):

bash
curl -X PUT http://127.0.0.1:8000/api/usuarios/1/ -H "Content-Type: application/json" -d '{"nombre":"Juan","apellido":"Pérez","email":"juan.perez@example.com","edad":30}'
DELETE (Eliminar):

bash
curl -X DELETE http://127.0.0.1:8000/api/usuarios/1/
