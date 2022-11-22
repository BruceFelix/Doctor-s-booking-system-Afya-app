from django.urls import path
from main import views

urlpatterns = [
    path('registerAdmin/', views.adminRegisterPage, name="admin-register"),
    path('registerPatient/', views.patientRegisterPage, name="pat-register"),
    path('registerDoctor/', views.doctor_signup_page, name="doc-register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('', views.landing, name='landing'),
    path('account/', views.PatientAccountSettings, name="account")
    # path('landing', views.landing, name='landing'),
    # path('doctor', views.doctor, name="doctor"),
    # path('patient', views.patient, name="patient"),
    # path('sign_up', views.sign_up, name="sign_up"),
    # path('signup', views.signup, name="signup"),
    # path('patientsignup', views.patient_signup, name="patient_signup"),
    # path('doctorssignup', views.doctor_signup, name="doctor_signup"),

]
