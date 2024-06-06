from .models import AddProduct
from django import forms

class AddProductForm(forms.ModelForm):
    class Meta:
        model=AddProduct
        fields="__all__"