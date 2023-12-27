from rest_framework import serializers
from .models import Postagem, Comentario
from django.contrib.auth.models import User

class PostarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Postagem
        fields = ['id', 'autor','conteudo', 'data_criacao', 'data_atualizacao']


class PostagemSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(write_only=True)

    class Meta:
        model = Postagem
        fields = ['id', 'autor', 'autor_username', 'conteudo', 'data_criacao', 'data_atualizacao']

    def create(self, validated_data):
        autor_username = validated_data.pop('autor_username', None)
        autor = User.objects.get(username=autor_username)
        postagem = Postagem.objects.create(autor=autor, **validated_data)
        return postagem

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'postagem', 'autor', 'conteudo', 'data_criacao', 'data_atualizacao']
