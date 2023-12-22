from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Postagem(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postagens')
    conteudo = models.TextField(max_length=140) # 140 caracteres é o limite do Twitter (old times)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Postagem por {self.autor.username} em {self.data_criacao}"

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    conteudo = models.TextField(max_length=140)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comentário por {self.autor.username} em {self.data_criacao}"
