from rest_framework import serializers

from .models import Moderador, Usuario

class ModeradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderador
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'