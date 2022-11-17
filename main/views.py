from django.shortcuts import render,redirect
from . forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate

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
    return render(request, 'registration/doctorssignup.html')