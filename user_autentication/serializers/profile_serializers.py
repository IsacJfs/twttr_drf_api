from rest_framework import serializers
from user_autentication.models import Profile
from .user_serializers import UserSerializer


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
        user = self.context["request"].user
        if user.is_authenticated:
            return obj.followers.filter(id=user.profile.id).exists()
        return False

    def get_username(self, obj):
        return obj.user.username

    def get_following_username(self, obj):
        return [profile.user.username for profile in obj.following.all()]
