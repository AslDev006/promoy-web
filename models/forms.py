from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import  AdviceModel

class AdviceForm(forms.ModelForm):
    class Meta:
        model = AdviceModel
        fields = ['name', 'address', 'phone_number', 'message']

class ProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    phone_number = PhoneNumberField(region="UZ")
    count = forms.IntegerField()