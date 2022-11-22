from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(User):
    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    # email = models.EmailField(unique=True)
    patient_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True, related_name='Patient')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    mobile_number = models.CharField(max_length=10)
    # password = models.CharField(max_length=200, null=True)
    age = models.IntegerField()
    is_patient = models.BooleanField(default=False)
    
    def __str__(self):
        return self.patient_user.first_name

    class Meta:
        db_table = "Patient"


class Doctor(models.Model):
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
    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    is_doctor = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=10)
    specialities = models.CharField(max_length=255, choices=SPECIALITIES, null=True, blank=True)
    county = models.CharField(max_length=255, choices=COUNTIES, null=True)
    # doctoruser = models.OneToOneField(MyBaseUser, on_delete = models.CASCADE, primary_key= True, related_name="Doctor")
    is_verified = models.BooleanField(default=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)

    class Meta:
        db_table = "Doctor"

