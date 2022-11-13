from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'main/landing.html')

def doctor(request):
    return render(request, 'main/doctors.html')

def patient(request):
    return render(request, 'main/patients.html')

