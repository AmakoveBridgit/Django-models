from django.db import models
# from order.models import Order


# Create your models here.
class Delivery(models.Model):
    # order = models.OneToOneField(Order, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=20)
    deliverytime = models.DateTimeField(auto_now=True)
    isdelivered = models.BooleanField(default=False)






