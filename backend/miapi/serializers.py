from rest_framework import serializers

from .models import Moderador, Usuario, Reporte, Sector

class ModeradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderador
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'