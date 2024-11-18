from django.conf import settings
from django.db import models

class Apartment(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    has_parking = models.BooleanField(default=False)
    has_pets = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    has_gym = models.BooleanField(default=False)
    images = models.JSONField(default=list)  
    floor = models.IntegerField()
    letter = models.CharField(max_length=1)
    bathrooms = models.IntegerField()
    rooms = models.IntegerField()
    additional_info = models.TextField(blank=True, null=True)
    rating = models.FloatField()

    def __str__(self):
        return self.name

class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartment_images')
    image = models.ImageField(upload_to='apartment_images/')