from django.db import models
from django.contrib.auth.models import User
from posts.models import Postagem


class Comentario(models.Model):
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comentarios"
    )
    postagem = models.ForeignKey(
        Postagem, on_delete=models.CASCADE, related_name="comentarios"
    )
    conteudo = models.TextField(max_length=140)
    data_criacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(
        User, related_name="curtidas_comentarios", blank=True
    )

    def __str__(self):
        return f"Comentário por {self.autor.username} em {self.data_criacao}"
