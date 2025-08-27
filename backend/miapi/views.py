from django.shortcuts import render
from rest_framework import viewsets

from .models import Moderador, Usuario
from .serializers import ModeradorSerializer, UsuarioSerializer

class ModeradorViewSet(viewsets.ModelViewSet):
    queryset = Moderador.objects.all()
    serializer_class = ModeradorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer