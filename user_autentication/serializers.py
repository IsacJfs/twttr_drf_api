from rest_framework import serializers
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from .models import Profile

class CustomUserCreateSerializer(UserCreateSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta(UserCreateSerializer.Meta):
        fields = tuple(UserCreateSerializer.Meta.fields) + ('first_name', 'last_name',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        # Inclua outros campos do modelo User que você deseja expor

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    following_usernames = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="username", source="following"
    )

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "name",
            "description",
            "birthday",
            "profile_picture",
            "cover_picture",
            "following_usernames",
        ]
