from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from comments.models import Comentario
from comments.serializers import ComentarioCreateSerializer, ComentarioListSerializer, ComentarioCurtidaSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

# Create your views here.
class AdicionarComentarioView(CreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioCreateSerializer

class ListarComentariosView(ListAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioListSerializer

class DetalheComentarioView(RetrieveAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioListSerializer

class CurtirComentarioView(CreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioCurtidaSerializer

class CurtirComentarioView(UpdateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioCurtidaSerializer

    def patch(self, request, *args, **kwargs):
        comentario = self.get_object()
        user = request.user

        # Adiciona ou remove o usuário da lista de curtidas
        if user in comentario.curtidas.all():
            comentario.curtidas.remove(user)
        else:
            comentario.curtidas.add(user)

        return Response(self.get_serializer(comentario).data)