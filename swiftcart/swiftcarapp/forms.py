from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUsercreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, label="username", required=True)
    phone_contact = forms.CharField(max_length=15, required=True)  
    address = forms.CharField(max_length=30,  required=True) 
    gender = forms.ChoiceField( choices=CustomUser.GENDER_CHOICES,  required=True)
    email = forms.EmailField(max_length=50,  required=True)

    class Meta:
        model = CustomUser
        fields = ['username','phone_contact','address','gender','email']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    