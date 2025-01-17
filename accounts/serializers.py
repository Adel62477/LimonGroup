from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'role', 'email', 'username', 'date_created', 'is_active', 'is_admin', 'is_superuser']
        read_only_fields = ['id', 'date_created', 'is_active', 'is_admin', 'is_superuser']


class UserCreateAPISerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'role', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

# class UserSerializer(serializers.ModelSerializer):
#     model = User
#     fields = "__all__"
#     # read_only_fields = ('name',)
#     # extra_kwargs = {
#     #         'password': {'write_only': True},
#     #         'name': {'write_only': True},
#     #         }
