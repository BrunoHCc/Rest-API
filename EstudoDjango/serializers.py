from rest_framework import serializers
from Serial.models import Avaliacao, Cursos

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:

        extra_kargs = {
            'email': {'write_only': True}
        }

        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'criacao',
            'ativo'
        )

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Cursos

        fields= (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )

