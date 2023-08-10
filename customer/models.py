from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
  user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
  # one to one relationship

  firstname = models.CharField(max_length=100,null=True)
  lastname=models.CharField(max_length=100,null=True)
  emailaddress = models.CharField(max_length=200)
  password=models.IntegerField()
  phonenumber = models.CharField(max_length=20)
  customerID=models.IntegerField()  

 