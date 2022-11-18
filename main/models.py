from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyBaseUser(AbstractUser):
    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    password = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    mobile_number = models.CharField(max_length=10)
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
    COUNTIES = [
        ('Mombasa','Mombasa' ),
        ('Nairobi', 'Nairobi')
    ]
    specialties = models.CharField(max_length=255, choices=SPECIALITIES, null=True, blank=True)
    county = models.CharField(max_length=255, choices=COUNTIES, null=True)
    doctoruser = models.OneToOneField(MyBaseUser, on_delete = models.CASCADE, primary_key= True, related_name="Doctor")
    is_verified = models.BooleanField(default=False)
    class Meta:
        db_table = "Doctor"

class Patient(MyBaseUser):
    age = models.IntegerField()
    patientuser = models.OneToOneField(MyBaseUser, on_delete = models.CASCADE, primary_key= True, related_name="Patient")

    class Meta:
        db_table = "Patient"