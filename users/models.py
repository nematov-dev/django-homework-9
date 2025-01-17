from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)