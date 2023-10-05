"""
This file is used to register the models in the admin panel.
"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserAdmin(UserAdmin):
    # Define the fields that will be displayed in the admin view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    # Define the fields that can be used to filter the users in the admin view
    list_filter = ('is_staff', 'is_active')
    # Define the fields that can be used to search for users in the admin view
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # Define the fields that can be used to order the users in the admin view
    ordering = ('username',)

# Register the User model with the custom admin view
admin.site.register(User, CustomUserAdmin)
