from django.contrib import admin
from .models import Apartment

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'price', 'rating')
    list_filter = ('has_parking', 'has_pets', 'has_pool', 'has_gym', 'floor', 'rooms', 'bathrooms')
    search_fields = ('name', 'owner__email', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'owner', 'price', 'street_address', 'expenses', 'rating')
        }),
        ('Details', {
            'fields': ('description', 'floor', 'letter', 'bathrooms', 'rooms', 'additional_info')
        }),
        ('Amenities', {
            'fields': ('has_parking', 'has_pets', 'has_pool', 'has_gym')
        }),
    )