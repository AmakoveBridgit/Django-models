from django.db import models

class Cart(models.Model):
    customer_ID = models.IntegerField()
    list_of_items = models.IntegerField()
    quantity_of_items = models.CharField(max_length=6)
   

