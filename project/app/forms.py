from .models import AddProduct,Register
from django import forms

class AddProductForm(forms.ModelForm):
    class Meta:
        model=AddProduct
        fields="__all__"

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"