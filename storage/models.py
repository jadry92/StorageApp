"""
    Storage Model
"""

# Django
from django.db import models
from django.contrib.auth import get_user_model

# User Model
User = get_user_model()

TRANSACTION_OPTIONS = [(0, 'CREATE'), (1, 'EDIT'), (2, 'DELETE')]


class Stock(models.Model):
    """
        Stock Model
    """
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity}'

class Product(models.Model):
    """
        Product Model
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return f'{self.name}'

class Transaction(models.Model):
    """
        Transaction Model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    product_name = models.CharField(max_length=255)
    transaction_type = models.IntegerField(choices=TRANSACTION_OPTIONS)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.product_name}'
