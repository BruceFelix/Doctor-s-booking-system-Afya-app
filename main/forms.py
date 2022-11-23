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
    class Meta:
        model = Schedule
        fields = "__all__"
        exclude = ['doctor']
        
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
