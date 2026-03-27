from .models import *
# from django.contrib.auth.models import Users
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    Recipe_img=serializers.ImageField(required=False)
    class Meta:
        model=Recipes
        fields="__all__"
        
        
        
from django.contrib.auth.models import User   ###############---------##############
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

