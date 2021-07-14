from django import forms
from django.core.validators import EmailValidator

from .models import CarGuy



class CreateNewCarGuy(forms.Form):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=200, validators=[EmailValidator()], widget=forms.TextInput(attrs={'class': 'form-control'}))
    car = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


