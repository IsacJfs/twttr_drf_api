from django.urls import path

from . import views


urlpatterns = [
    path('profile/<str:username>/', views.DetalheProfile.as_view(), name='profile-detail'),
    path('profile/', views.ListaProfile.as_view(), name='profile-list'),
    path('profile/<str:username>/follow/', views.FollowView.as_view(), name='follow-profile'),
]
