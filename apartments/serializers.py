from apartments.models import Apartment
from rest_framework import serializers

from authentication.serializers import UserSerializer

class ApartmentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    
    floor = serializers.IntegerField(required=False, allow_null=True)
    letter = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    
    class Meta:
        model = Apartment
        fields = '__all__'

    def create(self, validated_data):
        apartment = Apartment.objects.create(**validated_data)
        return apartment

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance