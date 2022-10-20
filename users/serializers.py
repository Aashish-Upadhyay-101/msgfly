from rest_framework import serializers
from .models import User
from .exceptions import UserNotFoundException

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input-type": "password"})
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password", "password2"]
        

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        
        if password != password2:
            raise serializers.ValidationError("Password2 didn't match password")
        
        del attrs["password2"] # no longer need this after validation

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User 
        fields = ["email", "password"]
     
    def validate(self, attrs):
        email = attrs.get("email")

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise UserNotFoundException
        
        return attrs