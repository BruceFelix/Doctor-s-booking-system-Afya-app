from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, max_length=128)
    mobile_number = models.CharField(max_length=10)
    age = models.IntegerField()

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name
    


class Doctor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    SPECIALITIES = [
        ('Dermatologists', 'Dermatologists'),
        ('Cardiologists', 'Cardiologists'),
        ('Gastroenterologist', 'Gastroenterologist'),
        ('Physiotherapist', 'Physiotherapist'),
        ('Pharmacist', 'Pharmacist'),
        ('Orthopaedist', 'Orthopaedist'),
        ('Nephrologist', 'Nephrologist'),
        ('Neurologist', 'Neurologist'),
        ('Rectal Surgeons', 'Rectal Surgeons'),
        ('Anesthesiologists', 'Anesthesiologists'),
        ('Allergists/Immunologists', 'Allergists/Immunologists'),
        ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
    ]
    COUNTIES = (
        ('Mombasa', 'Mombasa'),
        ('Nairobi', 'Nairobi')
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, max_length=128)
    mobile_number = models.CharField(max_length=10, null=True)
    specialities = models.CharField(max_length=255, choices=SPECIALITIES, null=True, blank=True)
    county = models.CharField(max_length=255, choices=COUNTIES, null=True)
    is_verified = models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Appointment(models.Model):
    scheduled_time = models.DateField()
    patient = models.OneToOneField(Patient,null=True )
    
class Schedule(models.Model):
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]

    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE,null=True)
    monday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES,null=True)
    tuesday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES,null=True)
    wednesday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES,null=True)
    thursday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES,null=True)
    friday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES,null=True)
    print(doctor)

    def __str__(self):
        return f'Schedule for {self.monday}'