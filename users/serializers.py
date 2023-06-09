from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Usuários


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 
                  'last_name', 'email', 'password', 'groups']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ["id", "date_joined"]

# Grupos


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

