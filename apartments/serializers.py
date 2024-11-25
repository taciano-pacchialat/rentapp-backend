from apartments.models import Apartment, ApartmentImage
from rest_framework import serializers

from authentication.serializers import UserSerializer

class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = ['id', 'image']

class ApartmentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    images = ApartmentImageSerializer(many=True, required=False, read_only=True)
    
    floor = serializers.IntegerField(required=False, allow_null=True)
    letter = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    
    class Meta:
        model = Apartment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        images = request.FILES.getlist('images')

        apartment = Apartment.objects.create(**validated_data)

        for image in images:
            ApartmentImage.objects.create(apartment=apartment, image=image)
        return apartment

    def update(self, instance, validated_data):
        request = self.context.get('request')
        images = request.FILES.getlist('images')

        # Update apartment fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Add new images
        for image in images:
            ApartmentImage.objects.create(apartment=instance, image=image)
        return instance