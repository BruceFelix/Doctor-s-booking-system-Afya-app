from django.shortcuts import render,redirect
from . forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from .models import MyBaseUser, Doctor, Patient

# Create your views here.
def landing(request):
    return render(request, 'main/landing.html')

def doctor(request):
    return render(request, 'main/doctors.html')

def patient(request):
    return render(request, 'main/patients.html')

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/landing')
    else:
        form = RegistrationForm()
    return render(request, 'registration/sign_up.html', {'form':form})
    
def signup(request):
    return render(request, 'registration/signup.html', )

def patient_signup(request):
    return render(request, 'registration/patientsignup.html')

def doctor_signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['mail']
        phonenumber = request.POST['number']
        password = request.POST['password']
        gender = request.POST['gender']
        county = request.POST['county']
        
        doctoruser = MyBaseUser(
            password = password,
            first_name = firstname,
            last_name = lastname,
            email = email,
            gender = gender,
            mobile_number = phonenumber,
            is_doctor = True, 
            username= firstname + " " +lastname
            )
        doctoruser.save()
        doctor = Doctor(specialties = "Dentist", county = "Nairobi", doctoruser = doctoruser)
        doctor.save()
        print("saved")
    return render(request, 'registration/doctorssignup.html')