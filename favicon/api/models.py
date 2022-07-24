from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    # completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
# class UserLogin(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
    
      
#     def __str__(self):
#         return self.title