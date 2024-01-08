from django.urls import path
from .views import AdicionarComentarioView, ListarComentariosView, DetalheComentarioView, CurtirComentarioView

urlpatterns = [
    path('comentarios/adicionar/', AdicionarComentarioView.as_view(), name='adicionar-comentario'),
    path('comentarios/listar/', ListarComentariosView.as_view(), name='listar-comentarios'),
    path('comentarios/<int:pk>/', DetalheComentarioView.as_view(), name='detalhe-comentario'),
    path('comentarios/<int:pk>/curtir/', CurtirComentarioView.as_view(), name='curtir-comentario'),
]
