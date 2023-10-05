"""
    Storage forms
"""

# Django
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField( max_length=100)
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

