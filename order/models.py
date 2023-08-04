from django.db import models
from customer.models import Customer
from cart.models import Cart
from delivery.models import Delivery



class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

    date_of_order = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()
    Total_price = models.DecimalField(max_digits=5,decimal_places=2)
    product_ID = models.IntegerField()
    delivery = models.OneToOneField(Delivery,null=True,on_delete=models.CASCADE)


