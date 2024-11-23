from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    floor = models.IntegerField(blank=True)
    letter = models.CharField(max_length=1, blank=True)
    bathrooms = models.IntegerField()
    rooms = models.IntegerField()
    additional_info = models.TextField(blank=True, null=True)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    street_address = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartment_images')
    image = models.ImageField(upload_to='apartment_images/')