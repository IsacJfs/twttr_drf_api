from django.urls import path
from . import views

urlpatterns = [
    # URLs para Postagens
    path('postagens/', views.ListaPostagens.as_view(), name='lista_postagens'),
    path('postagens/adicionar/', views.AdicionarPostagem.as_view(), name='adicionar_postagem'),
    path('postagens/<int:pk>/', views.DetalhePostagem.as_view(), name='detalhe_postagem'),
    path('postagens/<str:username>/', views.PostagemPorUsuario.as_view(), name='postagens_usuario'),

    # URLs para Comentários
    path('postagens/<int:postagem_id>/comentarios/', views.ListaComentarios.as_view(), name='lista_comentarios'),
    path('postagens/<int:postagem_id>/comentarios/<int:pk>/', views.DetalheComentario.as_view(), name='detalhe_comentario'),
    path('postagens/<int:postagem_id>/comentarios/adicionar/', views.AdicionarComentario.as_view(), name='adicionar_comentario'),
]
