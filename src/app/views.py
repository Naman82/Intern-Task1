from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth,User
from django.contrib import messages

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
    users=User.objects.all()
    return render(request,'patient_home.html',{'users':users})

def doctor_home(request):
    users=User.objects.all()
    return render(request,'doctor_home.html',{'users':users})
    

def logout(request):
    auth.logout(request)
    return redirect('/')
