from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'dni', 'phone_number', 'is_admin')  
    search_fields = ('email', 'name', 'phone_number')  
