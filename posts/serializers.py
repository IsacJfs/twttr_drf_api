from rest_framework import serializers
from .models import Postagem, Comentario

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ['id', 'autor', 'conteudo', 'data_criacao', 'data_atualizacao']

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'postagem', 'autor', 'conteudo', 'data_criacao', 'data_atualizacao']
