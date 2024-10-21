
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


    

class Student(models.Model):
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='puser') 
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    rollno=models.IntegerField()
       