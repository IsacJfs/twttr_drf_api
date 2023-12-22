from django.urls import path
from . import views

urlpatterns = [
    # URLs para Postagens
    path('postagens/', views.ListaPostagens.as_view(), name='lista_postagens'),
    path('postagens/<int:pk>/', views.DetalhePostagem.as_view(), name='detalhe_postagem'),

    # URLs para Comentários
    path('postagens/<int:postagem_id>/comentarios/', views.ListaComentarios.as_view(), name='lista_comentarios'),
    path('postagens/<int:postagem_id>/comentarios/<int:pk>/', views.DetalheComentario.as_view(), name='detalhe_comentario'),
]
