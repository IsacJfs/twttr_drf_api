from rest_framework import serializers

from comments.models import Comentario
from .models import Postagem
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
        fields = ['id', 'autor', 'conteudo', 'data_criacao']

class PostagemFeedSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    curtidas_count = serializers.SerializerMethodField()
    autor_username = serializers.SerializerMethodField()
    autor_name = serializers.SerializerMethodField()

    class Meta:
        model = Postagem
        fields = ['id', 'autor', 'autor_username','autor_name', 'conteudo', 'data_criacao', 'data_atualizacao', 'comentarios', 'curtidas_count']

    def get_curtidas_count(self, obj):
        return obj.curtidas.count()

    def get_autor_username(self, obj):
        return obj.autor.username
    
    def get_autor_name(self, obj):
        return obj.autor.first_name + ' ' + obj.autor.last_name