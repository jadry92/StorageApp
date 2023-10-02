"""
    Storage forms
"""

# Django
from django import forms

# Models
from storage.models import Product, Stock, Transaction

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    SKU = forms.CharField( max_length=100)
    quantity = forms.IntegerField()
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        """
            This method is used to add extra arguments to the form.
        """
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_quantity(self):
        """
            This method is used to validate the quantity field.
        """
        value = self.cleaned_data['quantity']
        if value <= 0:
            raise forms.ValidationError("Value should be greater than 0")
        return value

    def save(self):
        """
            This method is used to save the product.
        """
        data = self.cleaned_data

        stock = Stock.objects.create(
            quantity=data['quantity']
        )
        product = Product.objects.create(
            name=data['name'],
            description=data['SKU'],
            image=data['image'],
            stock=stock
        )
        description = f'{self.user.username} Create - {product.name} with {data["quantity"]} units'
        Transaction.objects.create(
            user=self.user,
            product=product,
            transaction_type=0,
            description=description
        )
        return product
