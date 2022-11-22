from django.shortcuts import render,redirect
from . forms import PatientForm
from django.contrib.auth import login, logout, authenticate
from . models import *
# Create your views here.
def landing(request):
    return render(request, 'main/landing.html')

def doctor(request):
    return render(request, 'main/doctors.html')

def patient(request):
    return render(request, 'main/patients.html')

def sign_up(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/landing')
    else:
        form = PatientForm()
    return render(request, 'registration/sign_up.html', {'form':form})
    
def signup(request):
    return render(request, 'registration/signup.html', )

def patient_signup(request):
    # if request.method == "POST":
    #     firstname = request.POST['firstname']
    #     lastname = request.POST['lastname']
    #     email = request.POST['mail']
    #     phonenumber = request.POST['number']
    #     age = request.POST['age']
    #     gender = request.POST['gender']
    #     password = request.POST['password']  

    #     newpatient = MyBaseUser(
    #         first_name = firstname,
    #         last_name = lastname,
    #         email = email,
    #         gender = gender,
    #         mobile_number = phonenumber,
    #         is_patient = True, 
    #         username= firstname + " " +lastname,
    #         password = password,
    #         )
    #     newpatient.save()
    #     patient = Patient(age = age, patientuser = newpatient)
    #     patient.save()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            age = form.cleaned_data.get('age')
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")

            user_patient = User.objects.get(username=username)
            patient_data = Patient.objects.create(
                username = first_name,
                first_name = first_name,
                last_name = last_name,
                email = email,
                patient_user = user_patient,
                is_patient = True,
                mobile_number=phone,
                gender=gender,
                age=age)
            patient_data.save()
            return render(request, 'registration/login.html')
    else:
        form =PatientForm()
    return render(request, 'registration/patientsignup.html', {'form': form})

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