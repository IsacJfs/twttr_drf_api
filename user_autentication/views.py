from rest_framework.generics import ListAPIView, RetrieveAPIView
from user_autentication.serializers import ProfileSerializer
from .models import Profile

class DetalheProfile(RetrieveAPIView):
    """
    View para detalhar um perfil de usuário.
    Para exibir todos os perfis de usuários, use a view ListaProfile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ListaProfile(ListAPIView):
    """
    View para listar todos os perfis de usuários.
    Para detalhar um perfil de usuário, use a view DetalheProfile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer