from apartments.models import Apartment, ApartmentImage
from rest_framework import serializers

class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = ['id', 'image']

class ApartmentSerializer(serializers.ModelSerializer):
    images = ApartmentImageSerializer(source='apartment_images', many=True, read_only=True)
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