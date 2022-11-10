from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def doctorssignup(request):
    return render(request, 'doctorssignup.html')

def doctors(request):
    return render(request, 'doctors.html')

def patients(request):
    return render(request, 'patients.html')
