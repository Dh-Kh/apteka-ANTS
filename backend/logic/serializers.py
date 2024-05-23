from rest_framework import serializers
from .models import EmployeeModel
from django.contrib.auth.models import User

class EmployeeModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeModel
        fields = ["full_name", "position", "email", "joined"]
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "email", "password",]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"]
            )
        user.set_password(validated_data["password"])
        user.save()
        return user
    
class DisplayUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username",]