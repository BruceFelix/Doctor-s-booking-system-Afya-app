from django.urls import path 
from main import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name="patient"),
]