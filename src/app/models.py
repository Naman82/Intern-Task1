from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    profile_pic=models.ImageField(upload_to="profile",null=True, blank=True)
    state=models.CharField(max_length=100, blank=True)
    city=models.CharField(max_length=100, blank=True)
    pincode=models.CharField(max_length=100, blank=True)

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(blank=True,max_length=150)
    category=models.CharField(blank=True,max_length=52)
    summary=models.TextField(blank=True, null=True)
    content=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='post/images', blank=True, null=True)
    is_draft=models.BooleanField(default=False)


class Appointment(models.Model):
    doctor_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_doctor')
    patient_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_patient')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_end_time = models.TimeField()