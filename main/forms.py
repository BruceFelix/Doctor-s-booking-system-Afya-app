from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class AdminSigupForm(ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username', 'email', 'password']
        widgets = {
        'password': forms.PasswordInput()
        }

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        exclude = ['user', 'is_verified']

class DoctorScheduleForm(ModelForm):
    STATUS_CHOICE = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]

    monday = forms.CharField(label='Monday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    tuesday = forms.CharField(label='Tuesday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    wednesday = forms.CharField(label='Wednesday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    thursday = forms.CharField(label='Thursday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    friday = forms.CharField(label='Friday', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Schedule
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        
class DoctorUserForm(ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username', 'email', 'password']
        widgets = {
        'password': forms.PasswordInput()
        }      
class PatientUserForm(ModelForm):
    class Meta:
        model= User
        fields=['first_name','last_name','username', 'email', 'password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['gender','mobile_number','age']
