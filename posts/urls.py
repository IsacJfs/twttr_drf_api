from django.urls import path
from . import views

urlpatterns = [
    # URLs para Postagens
    path('postagens/', views.PostagemFeedView.as_view(), name='lista_postagens'),
    path('postagens/adicionar/', views.AdicionarPostagem.as_view(), name='adicionar_postagem'),
    path('postagens/<int:pk>/', views.DetalhePostagem.as_view(), name='detalhe_postagem'),
    path('postagens/<str:username>/', views.PostagemPorUsuario.as_view(), name='postagens_usuario'),
]
