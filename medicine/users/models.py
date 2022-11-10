from django.db import models
from phone_field import PhoneField
# Create your models here.
class Person(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    # profile_pic = models.ImageField(null=True, blank=True)
    # phone = PhoneField(blank=True, help_text='Contact phone number')
class Doctor(Person):
    CITY_OPTIONS =(
        ('N', 'Nairobi'),
        ('M', 'Mombasa'),
    )
    Speciality = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname +" " + self.lastname


class Patient(Person):
    date_of_birth = models.DateField(null=True)
    def __str__(self):
        return self.firstname +" " + self.lastname

class Appointment(models.Model):
    scheduled_time = models.DateField()
    # patient = models.OneToOneField(d)
    # doctor = models.OneToOneField()
    
class Schedule(models.Model):
    # schedule = models.DateField()
    # doctor = models.OneToOneField()
    pass