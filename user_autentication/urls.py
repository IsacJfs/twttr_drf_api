from django.urls import path

from . import views


urlpatterns = [
    path('profile/<str:username>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/', views.ProfileListView.as_view(), name='profile-list'),
    path('profile/<str:username>/is-following/', views.IsFollowView.as_view(), name='follow-profile'),
]
