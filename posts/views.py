from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Postagem
from .serializers import PostagemFeedSerializer, PostagemSerializer, PostarSerializer, CurtirSerializer, CurtirPostagemSerializer
from django.contrib.auth.models import User

class PostagemPorUsuario(ListAPIView):
    serializer_class = PostagemFeedSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = User.objects.get(username=username)
        return Postagem.objects.filter(autor=user).prefetch_related('comentarios')

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

class CurtirPostagem(CreateAPIView):
    queryset = Postagem.objects.all()
    serializer_class = CurtirSerializer

class CurtirPostagemView(APIView):
    def post(self, request, pk):
        postagem = Postagem.objects.get(pk=pk)
        serializer = CurtirPostagemSerializer(
            postagem, 
            data=request.data, 
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)