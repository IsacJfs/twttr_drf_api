from rest_framework import serializers
from django.contrib.auth.models import User
from user_autentication.models import Profile

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