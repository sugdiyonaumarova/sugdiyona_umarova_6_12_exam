from django import forms
from .models import Product, Customer

class ProductForm(forms.ModelForm):
    delete = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'rating',
            'amount',
            'discount',
            'attribute',
        ]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']