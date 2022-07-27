from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

# class User(models.Model):
class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200 , unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    title=None
    # last_login = models.CharField(default=datetime.datetime.now(),max_length=200)
    # completed = models.BooleanField(default=False)
    USERNAME_FIELD ='username'
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return self.title
    
# class UserLogin(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
    
      
#     def __str__(self):
#         return self.title