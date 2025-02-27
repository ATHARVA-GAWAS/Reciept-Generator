from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Receipt

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class ReceiptForm(forms.ModelForm):
    class Meta:
        model=Receipt
        fields=['name','price','quantity']

