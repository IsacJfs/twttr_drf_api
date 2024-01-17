from rest_framework.generics import ListAPIView, RetrieveAPIView
from user_autentication.serializers.profile_serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from user_autentication.models import Profile


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
