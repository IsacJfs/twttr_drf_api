from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Postagem, Comentario
from .serializers import PostagemSerializer, ComentarioSerializer

class ListaPostagens(ListAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class DetalhePostagem(RetrieveAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class ListaComentarios(ListAPIView):
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.filter(postagem_id=self.kwargs['postagem_id'])

class DetalheComentario(RetrieveAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
