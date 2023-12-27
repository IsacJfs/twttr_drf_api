from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Postagem, Comentario
from .serializers import PostagemSerializer, ComentarioSerializer, PostarSerializer
from django.contrib.auth.models import User

class PostagemPorUsuario(ListAPIView):
    serializer_class = PostagemSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = User.objects.get(username=username)
        return Postagem.objects.filter(autor=user)

class ListaPostagens(ListAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class DetalhePostagem(RetrieveAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class AdicionarPostagem(CreateAPIView):
    serializer_class = PostarSerializer

class ListaComentarios(ListAPIView):
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.filter(postagem_id=self.kwargs['postagem_id'])

class DetalheComentario(RetrieveAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class AdicionarComentario(CreateAPIView):
    serializer_class = ComentarioSerializer
