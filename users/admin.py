"""
This file is used to register the models in the admin panel.
"""

# Django
from django.contrib import admin

# Models
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
        User Admin
    """
    pass
