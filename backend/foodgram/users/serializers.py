from .models import User
from rest_framework import serializers
from recipes.models import Follow


class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name'
        )

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Пользователь с таким email уже существует'
            )
        return email

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Пользователь с таким ником уже существует'
            )
        return username

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return (user.is_authenticated and
                Follow.objects.filter(user=user, author=obj).exists())
