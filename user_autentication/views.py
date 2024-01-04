from rest_framework.generics import ListAPIView, RetrieveAPIView
from user_autentication.serializers import ProfileSerializer, FollowSerializer
from rest_framework import views, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Profile

class DetalheProfile(RetrieveAPIView):
    """
    View para detalhar um perfil de usuário.
    Para exibir todos os perfis de usuários, use a view ListaProfile.
    """
    serializer_class = ProfileSerializer

    def get_object(self):
        """
        Retorna o perfil do usuário com base no username passado na URL.
        """
        username = self.kwargs.get('username')
        return get_object_or_404(Profile, user__username=username)

class ListaProfile(ListAPIView):
    """
    View para listar todos os perfis de usuários.
    Para detalhar um perfil de usuário, use a view DetalheProfile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class FollowView(views.APIView):
    """
    View para adicionar seguidor
    """
    def post(self, request, username):
        try:
            profile_to_follow = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            return Response({"error": "Perfil não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FollowSerializer(data=request.data, instance=profile_to_follow, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

