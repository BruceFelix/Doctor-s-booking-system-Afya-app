from django.urls import path
from main import views

urlpatterns = [
    path('registerAdmin/', views.adminRegisterPage, name="admin-register"),
    path('registerPatient/', views.patientRegisterPage, name="pat-register"),
    path('registerDoctor/', views.doctor_signup_page, name="doc-register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('landing/', views.landing, name="landing"),
    path('signup', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('account/', views.PatientAccountSettings, name="account"),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name="patient"),
    path('appointment', views.appointment, name='appointment'),
    path('schedule', views.schedule, name='schedule'),
]
