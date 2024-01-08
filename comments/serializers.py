from rest_framework import serializers
from .models import Comentario
from django.contrib.auth.models import User

class ComentarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['autor', 'postagem', 'conteudo']
    
class ComentarioListSerializer(serializers.ModelSerializer):
    curtidas_count = serializers.SerializerMethodField()

    class Meta:
        model = Comentario
        fields = ['id', 'autor', 'postagem', 'conteudo', 'data_criacao', 'curtidas_count']

    def get_curtidas_count(self, obj):
        return obj.curtidas.count()

class ComentarioCurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['curtidas']
