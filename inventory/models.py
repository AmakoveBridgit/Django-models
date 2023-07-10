from django.db import models
from vendor.models import Vendor
class Product(models.Model):
    Vendor=models.ForeignKey(Vendor,null=True,on_delete=models.CASCADE)
           
    name=models.CharField(max_length=32)
    price =models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(max_length=255, default="No description available")

    image =models.ImageField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated =models.DateTimeField(auto_now=True)
    stock=models.PositiveIntegerField()

