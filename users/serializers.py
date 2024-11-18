from rest_framework import serializers
from .models import User
from apartments.models import Apartment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

