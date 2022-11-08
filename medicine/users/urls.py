from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('doctorssignup/', views.doctorssignup, name='doctorssignup'),
    path('doctors/', views.doctors, name='doctors'),
    path('patients/', views.patients, name='patients'),
]