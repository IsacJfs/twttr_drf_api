from django.contrib.auth.models import User
from user_autentication.models import Profile
from user_autentication.serializers import profile_serializers
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request):
    user_to_follow = request.data.get('username')
    user_to_follow = get_object_or_404(Profile, user__username=user_to_follow)

    user_profile = Profile.objects.get(user=request.user)
    
    if user_profile == user_to_follow:
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    # Assuming a many-to-many field named 'followers' in the User model
    if user_to_follow.followers.filter(id=user_profile.id).exists():
        return Response({"error": "Already following."}, status=status.HTTP_400_BAD_REQUEST)

    user_to_follow.followers.add(user_profile)
    return Response({"success": "User followed."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request):
    user_to_unfollow = request.data.get('username')
    user_to_unfollow = get_object_or_404(Profile, user__username=user_to_unfollow)

    user_profile = Profile.objects.get(user=request.user)

    if not user_to_unfollow.followers.filter(id=user_profile.id).exists():
        return Response({"error": "Not following this user."}, status=status.HTTP_400_BAD_REQUEST)

    user_to_unfollow.followers.remove(user_profile)
    return Response({"success": "User unfollowed."}, status=status.HTTP_200_OK)
