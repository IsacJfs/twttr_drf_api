from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Postagem
from .serializers import PostagemFeedSerializer, PostagemSerializer, PostarSerializer
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

class PostagemFeedView(ListAPIView):
    queryset = Postagem.objects.all().prefetch_related('comentarios')
    serializer_class = PostagemFeedSerializer