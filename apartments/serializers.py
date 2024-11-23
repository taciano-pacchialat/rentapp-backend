from apartments.models import Apartment, ApartmentImage
from rest_framework import serializers

from authentication.serializers import UserSerializer

class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = ['id', 'image']

class ApartmentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    images = ApartmentImageSerializer(source='apartment_images', many=True, read_only=True)
    
    floor = serializers.IntegerField(required=False, allow_null=True)
    letter = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    
    class Meta:
        model = Apartment
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        if len(images_data) > 20:
            raise serializers.ValidationError("Maximum 20 images allowed.")
        apartment = Apartment.objects.create(**validated_data)
        for image_data in images_data:
            ApartmentImage.objects.create(apartment=apartment, **image_data)
        return apartment