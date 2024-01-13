from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Postagem

class CurtirPostagemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.postagem = Postagem.objects.create(title='Test Post', content='This is a test post')

    def test_curtir_postagem(self):
        url = reverse('curtir-postagem', kwargs={'pk': self.postagem.pk})
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.postagem.refresh_from_db()
        self.assertTrue(self.postagem.curtido)

    def test_curtir_postagem_unauthenticated(self):
        self.client.logout()
        url = reverse('curtir-postagem', kwargs={'pk': self.postagem.pk})
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.postagem.refresh_from_db()
        self.assertFalse(self.postagem.curtido)