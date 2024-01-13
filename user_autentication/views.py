from rest_framework.generics import ListAPIView, RetrieveAPIView
from user_autentication.serializers import ProfileSerializer, FollowSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import views, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Profile

class ProfileDetailView(RetrieveAPIView):
    """
    View para detalhar um perfil de usuário.
    Para exibir todos os perfis de usuários, use a view ListaProfile.
    """
    serializer_class = ProfileSerializer
    def get_object(self):
        username = self.kwargs.get("username")
        return get_object_or_404(Profile, user__username=username)

class ProfileListView(ListAPIView):
    """
    View para listar todos os perfis de usuários.
    Para detalhar um perfil de usuário, use a view DetalheProfile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class IsFollowView(views.APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        target_profile = get_object_or_404(Profile, user__username=username)
        user_profile = request.user.profile
        is_following = target_profile.followers.filter(username=user_profile.username).exists()
        return Response({'is_following': is_following}, status=status.HTTP_200_OK)

