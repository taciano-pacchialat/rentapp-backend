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
        # Extract images from the request
        request = self.context.get('request')
        images = request.FILES.getlist('images')

        # Create the Apartment instance
        apartment = Apartment.objects.create(**validated_data)

        # Create ApartmentImage instances
        for image in images:
            ApartmentImage.objects.create(apartment=apartment, image=image)
        return apartment