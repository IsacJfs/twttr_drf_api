from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Postagem

class CurtirPostagemTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.postagem = Postagem.objects.create(conteudo='Postagem de teste', autor=self.user)
        self.url_curtir = reverse('curtir_postagem', kwargs={'pk': self.postagem.pk})
        # self.url_descurtir = reverse('descurtir_postagem', kwargs={'pk': self.postagem.pk})
        self.client.force_authenticate(user=self.user)

    def test_curtir_postagem(self):
        response = self.client.post(self.url_curtir)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_descurtir_postagem(self):
    #     # Primeiro, curtir a postagem
    #     self.client.post(self.url_curtir)
    #     # Depois, tentar descurtir
    #     response = self.client.post(self.url_descurtir)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
