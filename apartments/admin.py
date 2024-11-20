from django.contrib import admin
from .models import Apartment, ApartmentImage

class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'price', 'rating')
    list_filter = ('has_parking', 'has_pets', 'has_pool', 'has_gym', 'floor', 'rooms', 'bathrooms')
    search_fields = ('name', 'owner__email', 'description')
    inlines = [ApartmentImageInline]
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

@admin.register(ApartmentImage)
class ApartmentImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartment', 'image')