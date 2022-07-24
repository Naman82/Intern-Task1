from django.urls import path
from app import views

urlpatterns=[
    path('',views.index,name='index'),
    path('patient/',views.patient,name='patient'),
    path('doctor/',views.doctor,name='doctor'),
    path('patient/login/',views.patient_login,name='patient_login'),
    path('doctor/login/',views.doctor_login,name='doctor_login'),
    path('patient/home/',views.patient_home,name='patient_home'),
    path('doctor/home/',views.doctor_home,name='doctor_home'),
    path('logout/',views.logout,name='logout'),
]