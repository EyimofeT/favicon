from turtle import title
from django.db import models
import datetime
# Create your models here.

# class User(models.Model):
class ImageUpload(models.Model):
    user_id = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    created_at=models.CharField(default=datetime.datetime.now(),max_length=200)
    
    def nameFile(instance,Filename):
        return '/'.join(['images',str(instance.user_id),Filename])
    
    upload_to=nameFile
    
    def __str__(self):
        return self.title
    