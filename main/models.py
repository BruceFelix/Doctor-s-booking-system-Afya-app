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
    # patient = models.OneToOneField(d)
    # doctor = models.OneToOneField()
    
# class Schedule(models.Model):
#     DAYS_OF_THE_WEEK = [
#         ('Monday', 'Monday'),
#         ('Tuesday', 'Tuesday'),
#         ('Wednesday', 'Wednesday'),
#         ('Thursday', 'Thursday'),
#         ('Friday', 'Friday'),
#     ]
#     schedule = models.CharField(max_length=255, choices=DAYS_OF_THE_WEEK, null=True)
#     doctor = models.OneToOneField(Doctor, null=True, on_delete=models.CASCADE)
#     # print(self.doctor)

#     def __str__(self):
#         return f'Schedule for {self.doctor}'
class Schedule(models.Model):
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]

    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    monday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    tuesday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    wednesday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    thursday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    friday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    saturday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    sunday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)

    def __str__(self):
        return f'Schedule for {self.doctor.user.first_name}'