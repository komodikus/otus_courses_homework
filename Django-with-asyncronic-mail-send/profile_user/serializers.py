from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        user = Profile(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Profile
        fields = ['username', 'password', 'email', 'courses']
        extra_kwargs = {'password': {'write_only': True}}



