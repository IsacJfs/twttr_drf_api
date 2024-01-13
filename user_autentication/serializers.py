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
    username = serializers.SerializerMethodField()
    is_following = serializers.SerializerMethodField()
    following_username = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "username",
            "description",
            "birthday",
            "profile_picture",
            "cover_picture",
            "following_username",
            "followers_count",
            "is_following",  # novo campo
        ]
    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_is_following(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.followers.filter(id=user.profile.id).exists()
        return False
    
    def get_username(self, obj):
        return obj.user.username
    
    def get_following_username(self, obj):
        return [profile.user.username for profile in obj.following.all()]

class FollowSerializer(serializers.ModelSerializer):
    follower_id = serializers.CharField(write_only=True)
    action = serializers.CharField(write_only=True)

    class Meta:
        model = Profile
        fields = ['follower_id', 'action']

    def validate(self, data):
        # Validação adicional para garantir que 'action' é 'follow' ou 'unfollow'
        if data['action'] not in ['follow', 'unfollow']:
            raise serializers.ValidationError("Ação inválida. Use 'follow' ou 'unfollow'.")
        return data

    def save(self, **kwargs):
        follower_id = self.validated_data['follower_id']
        action = self.validated_data['action']
        follower = User.objects.get(id=follower_id)

        if action == 'follow':
            # Lógica para seguir um usuário
            if self.instance.following.filter(id=follower.profile.id).exists():
                raise serializers.ValidationError("Você já está seguindo este usuário.")
            self.instance.following.add(follower.profile)
        elif action == 'unfollow':
            # Lógica para deixar de seguir um usuário
            if not self.instance.following.filter(id=follower.profile.id).exists():
                raise serializers.ValidationError("Você não está seguindo este usuário.")
            self.instance.following.remove(follower.profile)

        return self.instance
