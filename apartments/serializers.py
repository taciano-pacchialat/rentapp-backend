from apartments.models import Apartment
from rest_framework import serializers


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'