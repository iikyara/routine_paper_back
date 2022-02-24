from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import FirebaseUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", "something")
        user = get_user_model()(password=make_password(password), **validated_data)
        user.save()
        return user


class FirebaseUserSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseUser
        fields = ("id", "screen_name", "email", "picture", "date_joined")
        read_only_fields = ("id", "email", "date_joined")


class FirebaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseUser
        fields = ("id", "screen_name", "picture", "date_joined")
        read_only_fields = ("id", "screen_name", "picture", "date_joined")
