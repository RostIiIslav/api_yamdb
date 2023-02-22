from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.constants import CONF_CODE_MAX_LEN, EMAIL_MAX_LEN, USERNAME_MAX_LEN
from users.validators import not_me_username_validator, username_validator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )


class UserProfileSerializer(UserSerializer):
    """Сериализатор модели User для профиля пользователя."""

    class Meta(UserSerializer.Meta):
        read_only_fields = ("role",)


class SignUpSerializer(serializers.Serializer):
    """Сериализатор для регистрации."""

    username = serializers.CharField(
        max_length=USERNAME_MAX_LEN,
        required=True,
        validators=[not_me_username_validator, username_validator],
    )
    email = serializers.EmailField(
        max_length=EMAIL_MAX_LEN,
        required=True,
    )

    def validate(self, data):
        if self.context['request'].method == 'POST':
            username = self.context.get('view').kwargs.get('username')
            email = self.context.get('view').kwargs.get('email')
            if User.objects.filter(username=username, email=email).exists():
                raise serializers.ValidationError(
                    "Данное имя пользователя или email "
                    "уже используются"
                )
        return data


class GetAuthTokenSerializer(serializers.Serializer):
    """Сериализатор для получения токена."""

    username = serializers.CharField(
        max_length=USERNAME_MAX_LEN,
        required=True,
        validators=[not_me_username_validator, username_validator],
    )
    confirmation_code = serializers.CharField(
        required=True, max_length=CONF_CODE_MAX_LEN
    )