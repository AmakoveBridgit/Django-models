from django.db import models

class Customer(models.Model):
  Firstname = models.CharField(max_length=100)
  Secondname=models.CharField(max_length=100)
  Emailaddress = models.CharField(max_length=200)
  password=models.IntegerField()
  phoneNumber = models.CharField(max_length=20)
  customerID=models.IntegerField()  

