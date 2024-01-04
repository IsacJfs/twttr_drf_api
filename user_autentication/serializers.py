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
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    following_usernames = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="username", source="following"
    )

    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "description",
            "birthday",
            "profile_picture",
            "cover_picture",
            "following_usernames",
            "followers_count",
        ]

    def get_followers_count(self, obj):
        return obj.followers.count()

class FollowSerializer(serializers.ModelSerializer):
    follower_username = serializers.CharField(write_only=True)

    class Meta:
        model = Profile
        fields = ['follower_username']

    def validate_follower_username(self, value):
        if value == self.context['request'].user.username:
            raise serializers.ValidationError("Não é possível seguir a si mesmo.")
        try:
            User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuário não encontrado.")
        return value

    def save(self, **kwargs):
        follower_username = self.validated_data['follower_username']
        follower = User.objects.get(username=follower_username)
        # Verifica se o perfil já está seguindo o usuário
        if self.instance.following.filter(id=follower.profile.id).exists():
            raise serializers.ValidationError("Você já está seguindo este usuário.")
        self.instance.following.add(follower.profile)
        return self.instance
