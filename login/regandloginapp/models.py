from django.db import models
class Reg(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    user=models.CharField(primary_key=True,max_length=20)
    pwd=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10,unique=True)
    email=models.EmailField(max_length=20,unique=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=20,blank=True,null=True)


class Login(models.Model):
    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)


# Create your models here.
