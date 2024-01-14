from django.urls import path

from .views.profile_views import ProfileListView, ProfileDetailView
from .views.follow_views import follow_user, unfollow_user


urlpatterns = [
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/', ProfileListView.as_view(), name='profile-list'),
    path('follow/', follow_user, name='follow-profile'),
    path('unfollow/', unfollow_user, name='unfollow-profile'),
]
