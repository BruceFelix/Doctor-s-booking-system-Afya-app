from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyBaseUser(AbstractUser):
    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    mobile_number = models.CharField(max_length=10, unique=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Doctor(MyBaseUser):
    SPECIALITIES = [
    ('Dermatologists', 'Dermatologists'),
    ('Cardiologists', 'Cardiologists'),
    ('Gastroenterologist', 'Gastroenterologist'),
    ('Physiotherapist', 'Physiotherapist'),
    ('Pharmacist','Pharmacist'),
    ('Orthopaedist', 'Orthopaedist'),
    ('Nephrologist', 'Nephrologist'),
    ('Neurologist', 'Neurologist'),
    ('Rectal Surgeons', 'Rectal Surgeons'),
    ('Anesthesiologists','Anesthesiologists'),
    ('Allergists/Immunologists', 'Allergists/Immunologists'),
    ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
]
    specialties = models.CharField(max_length=255, choices=SPECIALITIES, null=True, blank=True)

class Patient(MyBaseUser):
    age = models.IntegerField()