from django.contrib.auth.models import User
from rest_framework import serializers


# Usuários


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 
                  'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ["id", "date_joined"]
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user
