from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import exceptions
from requests import request
from app.models import Post,Appointment
import google_apis_oauth
from googleapiclient.discovery import build
from datetime import datetime,timedelta
# from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

User = get_user_model()

# Create your views here.
def index(request):
    return render(request,'index.html')

def patient(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        profile=request.FILES['photoInput']
        state=request.POST['state']
        city=request.POST['city']
        pincode=request.POST['pincode']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('patient')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('patient')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_patient=True,profile_pic=profile,state=state,city=city,pincode=pincode)
                user.save();
                return redirect('patient_login')

        else:
            messages.info(request,'Password does not match , Try again')
            return redirect('patient')
    else:
        return render(request,'patient_register.html')

def doctor(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        profile=request.FILES['photoInput']
        state=request.POST['state']
        city=request.POST['city']
        pincode=request.POST['pincode']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('doctor')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('doctor')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_doctor=True,profile_pic=profile,state=state,city=city,pincode=pincode)
                user.save();
                return redirect('doctor_login')

        else:
            messages.info(request,'Password does not match , Try again')
            return redirect('doctor')
    else:
        return render(request,'doctor_register.html')

def patient_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_patient==True:
                auth.login(request,user)
                return redirect('patient_home')
            else:
                messages.info(request,'Credentials Invalid')
                return redirect('patient_login')

        else:
            messages.info(request,'Credentials Invalid')
            return redirect('patient_login')
    else:
        return render(request,'patient_login.html')

def doctor_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_doctor==True:
                auth.login(request,user)
                return redirect('doctor_home')
            else:
                messages.info(request,'Credentials Invalid')
                return redirect('doctor_login')

        else:
            messages.info(request,'Credentials Invalid')
            return redirect('doctor_login')
    else:
        return render(request,'doctor_login.html')

def patient_home(request):
    return render(request,'patient_home.html')

def doctor_home(request):
    users=User.objects.all()
    return render(request,'doctor_home.html',{'users':users})
    

def logout(request):
    auth.logout(request)
    return redirect('/')


def post_form(request):
    if request.method == 'POST':
        title=request.POST['title']
        category=request.POST['category']
        content=request.POST['content']
        summary=request.POST['summary']
        image=request.FILES['photoInput']
        is_draft=request.POST['is_draft']

        post=Post(user=request.user,title=title,category=category,summary=summary,content=content,image=image,is_draft=is_draft)
        post.save()

    return render(request,'doctor_home.html')

def mental_health(request):
    posts=Post.objects.all()
    return render(request,'patient_home1.html',{'posts':posts})

def heart_disease(request):
    posts=Post.objects.all()
    return render(request,'patient_home2.html',{'posts':posts})

def covid_19(request):
    posts=Post.objects.all()
    return render(request,'patient_home3.html',{'posts':posts})

def immunization(request):
    posts=Post.objects.all()
    return render(request,'patient_home4.html',{'posts':posts})

def drafts(request):
    posts=Post.objects.all()
    return render(request,'doctor_posts.html',{'posts':posts})

def allposts(request):
    posts=Post.objects.all()
    return render(request,'doctor_allposts.html',{'posts':posts})

def draftpost(request):
    if request.method == 'POST':
        postid=request.POST['postid']
    post=Post.objects.get(pk=postid)
    post.is_draft=False
    post.save()
    return render(request,'doctor_home.html')


# import os
# import google_apis_oauth

# from django.shortcuts import HttpResponseRedirect

# # The url where the google oauth should redirect
# # after a successful login.
# REDIRECT_URI = 'http://localhost:8000/google_oauth/callback/'

# # Authorization scopes required
# SCOPES = ['https://www.googleapis.com/auth/calendar']

# # Path of the "client_id.json" file
# # JSON_FILEPATH = os.path.join(os.getcwd(), 'credentials.json')
# JSON_FILEPATH = r'D:\Assignment\src\app\credentials.json'

# def RedirectOauthView(request):
#     oauth_url = google_apis_oauth.get_authorization_url(
#         JSON_FILEPATH, SCOPES, REDIRECT_URI)
        
#     return HttpResponseRedirect(oauth_url)




# def CallbackView(request):
#     # try:
#     # Get user credentials
#     credentials = google_apis_oauth.get_crendentials_from_callback(
#         request,
#         r'D:\Assignment\src\app\credentials.json',
#         SCOPES,
#         REDIRECT_URI
#     )
#     # Stringify credentials for storing them in the DB
#     stringified_token = google_apis_oauth.stringify_credentials(credentials)
#     print(stringified_token)
#     # except:
#     #     print('error')
#     return render(request,'calender.html')


def appointment(request):
    data = User.objects.filter(is_doctor=True)
    print(data)
    return render(request, 'appointment.html', {'data': data})

def create_appointment(request):
    if request.method == 'POST':
        appointment_date=request.POST['date']
        appointment_time=request.POST['time']
        doctor_id=request.POST['doctor_id']
    doctor_name = User.objects.get(pk=doctor_id)
    first_name = doctor_name.first_name
    last_name = doctor_name.last_name
    full_name = str(first_name) + " " + str(last_name)
    location = doctor_name.city
    user=request.user
    end_time = calendar_app(full_name, appointment_date, appointment_time, location)
    appoint = Appointment(doctor_name=doctor_name, patient_name=user, apppointment_date=appointment_date, appointment_time=appointment_time, appointment_end_time=end_time)
    appoint.save()
    data = Appointment.objects.filter(patient_name=request.user)
    # print(doctor_name.first_name)
    # print(request.user)

    return render(request,'create_appointment.html',{'data':data})


# def create_appoint(request, pk):
#     doctor = User.objects.get(pk=pk)
#     first_name = doctor.first_name
#     last_name = doctor.last_name
#     full_name = str(first_name) + " " + str(last_name)
#     if request.method == 'POST':
#         form = AppointmentCreation(request.POST)
#         if form.is_valid():
#             app_date = form.cleaned_data['app_date']
#             location = doctor.City
#             user = request.user
#             docof = User.objects.get(Q(username=doctor.username))
#             app_time = form.cleaned_data['app_time']
#             speciality = form.cleaned_data['speciality']
#             end_time = calendar_app(full_name, app_date, app_time, location)
#             print(type(end_time))
#             appoint = Appointment(
#                 doctor_name=docof, patient_name=user, app_date=app_date, app_time=app_time, speciality=speciality, end_time=end_time)
#             appoint.save()
#             messages.success(
#                 request, 'Your Appointment has been scheduled')
#             data = Appointment.objects.filter(patient_name=request.user)
#             return render(request, 'viewappoints.html', {'data': data})
#         else:
#             msg = 'Errors while validating the form. Try Again!'
#             return render(request, 'appointform.html', {'form': form, 'msg': msg})
#     else:
#         form = AppointmentCreation()
#         return render(request, 'appointform.html', {'form': form, 'doctor': full_name})


def calendar_app(doctor, dateof, timeof, city):
    scopes = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file(
        "app\client_secret.json", scopes=scopes)
    # credentials = flow.run_console()
    # pickle.dump(credentials, open("token.pkl", "wb"))

    credentials = pickle.load(open("app/token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)
    result = service.calendarList().list().execute()
    calendar_id = result['items'][1]['id']
    result = service.events().list(calendarId=calendar_id).execute()

    date_of = dateof.strftime("%d")
    month_of = dateof.strftime("%m")
    year_of = dateof.strftime("%Y")
    hour_of = timeof.strftime("%H")
    min_of = timeof.strftime("%M")
    sec_of = timeof.strftime("%S")

    start_time = datetime(int(year_of), int(month_of), int(
        date_of), int(hour_of), int(min_of), int(sec_of))
    end_time = start_time + timedelta(minutes=45)
    timezone = 'Asia/Kolkata'

    description = "Appointment with Doctor " + str(doctor)

    event = {
        'summary': 'Doctor Appointment',
        'location': str(city),
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24*60},
                {'method': 'popup', 'minutes': 15},
            ],
        },
    }

    service.events().insert(calendarId=calendar_id, body=event).execute()

    return end_time



