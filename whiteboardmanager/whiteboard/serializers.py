from rest_framework import serializers
from .models import User
from .models import Board

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'