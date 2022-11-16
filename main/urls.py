from django.urls import path 
from main import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('landing', views.landing, name='landing'),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name="patient"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('signup', views.signup, name="signup"),
    path('patientsignup', views.patient_signup, name="patient_signup"),
    
]