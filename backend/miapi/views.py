from django.shortcuts import render
from rest_framework import viewsets

from .models import Moderador, Usuario, Reporte, Sector
from .serializers import ModeradorSerializer, UsuarioSerializer, ReporteSerializer, SectorSerializer

class ModeradorViewSet(viewsets.ModelViewSet):
    queryset = Moderador.objects.all()
    serializer_class = ModeradorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ReporteViewSer(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class SectorViewSer(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

