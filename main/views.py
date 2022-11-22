from django.shortcuts import render, redirect
from . forms import PatientUserForm, PatientForm, DoctorUserForm, DoctorForm, AdminSigupForm
from django.contrib.auth import login, logout, authenticate
from .models import Doctor, Patient
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your views here.


def landing(request):
    return render(request, 'main/landing.html')


def doctor(request):
    return render(request, 'main/doctors.html')


def patient(request):
    return render(request, 'main/patients.html')

def adminRegisterPage(request):
    form = AdminSigupForm()
    if request.method=='POST':
        form= AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return redirect('login')
    return render(request,'registration/adminsignup.html',{'form':form})


def patientRegisterPage(request):
    userForm = PatientUserForm()
    patientForm = PatientForm()

    if request.method == 'POST':
        userForm = PatientUserForm(request.POST)
        patientForm = PatientForm(request.POST, request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save()
            patient.user = user
            patient = patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return redirect('login')
    context = {'userForm': userForm, 'patientForm': patientForm}

    return render(request, 'registration/sign_up.html', context)


def doctor_signup_page(request):
    userForm = DoctorUserForm()
    doctorForm = DoctorForm()

    if request.method == 'POST':
        userForm = DoctorUserForm(request.POST)
        doctorForm = DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            doctor = doctorForm.save()
            doctor.user = user
            doctor = doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return redirect('login')
    context = {'userForm': userForm, 'doctorForm': doctorForm}
    return render(request, 'registration/doctor_signup.html', context)

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def PatientAccountSettings(request):
    # print(request)
    # patient = request
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'registration/patient_account_settings.html', context)
