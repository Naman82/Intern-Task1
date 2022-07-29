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
    path('doctor/post/',views.post_form,name='post_form'),
    path('patient/mental-health/',views.mental_health,name='mental_health'),
    path('patient/heart-disease/',views.heart_disease,name='heart_disease'),
    path('patient/covid-19/',views.covid_19,name='covid_19'),
    path('patient/immunization/',views.immunization,name='immunization'),
    path('doctor/drafts/',views.drafts,name='drafts'),
    path('doctor/posts/',views.allposts,name='allposts'),
    path('doctor/draftpost/',views.draftpost,name='draftpost'),
    # path('google_oauth/redirect/',views.RedirectOauthView, name='RedirectOauthView'),
    # path('google_oauth/callback/',views.CallbackView)
    # path('events/',views.events,name='events'),
    path('appointment/',views.appointment,name='appointment'),
    path('appointment/create/',views.create_appointment,name='create_appointment'),
]