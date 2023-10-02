"""
    Admin for storage app
"""

# Django
from django.contrib import admin

# models
from storage.models import Product, Stock, Transaction


@admin.register(Product, Stock, Transaction)
class AdminStore(admin.ModelAdmin):
    pass

