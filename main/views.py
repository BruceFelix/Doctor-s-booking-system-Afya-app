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
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['mail']
        phonenumber = request.POST['number']
        age = request.POST['age']
        gender = request.POST['gender']
        password = request.POST['password']  

        newpatient = MyBaseUser(
            first_name = firstname,
            last_name = lastname,
            email = email,
            gender = gender,
            mobile_number = phonenumber,
            is_patient = True, 
            username= firstname + " " +lastname,
            password = password,
            )
        newpatient.save()
        patient = Patient(age = age, patientuser = newpatient)
        patient.save()
        
    return render(request, 'registration/patientsignup.html')

def doctor_signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['mail']
        phonenumber = request.POST['number']
        speciality = request.POST['speciality']
        gender = request.POST['gender']
        county = request.POST['county']
        password = request.POST['password']  

        newdoctor = MyBaseUser(
            first_name = firstname,
            last_name = lastname,
            email = email,
            gender = gender,
            mobile_number = phonenumber,
            is_doctor = True, 
            username= firstname + " " +lastname,
            password = password,
            )
        newdoctor.save()
        doctor = Doctor(specialities = speciality, county = county, doctoruser = newdoctor)
        doctor.save()
    return render(request, 'registration/doctorssignup.html')