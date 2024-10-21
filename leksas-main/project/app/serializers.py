from rest_framework import serializers

from .models import Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields ='__all__'
