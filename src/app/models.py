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
