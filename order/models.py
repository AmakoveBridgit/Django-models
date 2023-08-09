from django.db import models
from customer.models import Customer
from cart.models import Cart
from delivery.models import Delivery



class Order(models.Model):

    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart,null=True,on_delete=models.CASCADE)
    date_of_order = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=5,decimal_places=2)
    # product_ID = models.IntegerField()
    # delivery_time = models.OneToOneField(Delivery,null=True,on_delete=models.CASCADE)


