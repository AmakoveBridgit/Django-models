from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
  user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
  # one to one relationship

  Firstname = models.CharField(max_length=100)
  Secondname=models.CharField(max_length=100)
  Emailaddress = models.CharField(max_length=200)
  password=models.IntegerField()
  phoneNumber = models.CharField(max_length=20)
  customerID=models.IntegerField()  

