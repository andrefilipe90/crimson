from rest_framework import serializers
from .models import Sala

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ('id', 'nome', 'quantidade_alunos', 'status', 'criacao', 'inicio', 'final' )