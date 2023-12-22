from django.urls import path

from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.DetalheProfile.as_view(), name='profile-detail'),
    path('profile/', views.ListaProfile.as_view(), name='profile-list'),
]
