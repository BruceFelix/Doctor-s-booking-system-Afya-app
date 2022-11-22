from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class PatientForm(UserCreationForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    username = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Password'}),
        )
    password2 = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Password Again'}),
        )
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your phone number'}))
    gender = forms.CharField(label='Choose your Gender', widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'input-field'}), required=True)
    age = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field', 'id':'birth_date', 'placeholder': 'Enter your age', 'autocomplete': 'off'}), required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone', 'gender', 'age']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Enter Email'})
        self.fields['first_name'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Enter Last Name'})