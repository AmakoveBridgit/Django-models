from django.db import models
from inventory.models  import Product



class Cart(models.Model):
    image=models.ImageField(upload_to='cart_images/',null=True)
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=7 ,decimal_places=2,default=0)
    products=models.ManyToManyField(Product)
    customer_ID = models.IntegerField()
    list_of_items = models.IntegerField()
    quantity_of_items = models.CharField(max_length=6)
   

