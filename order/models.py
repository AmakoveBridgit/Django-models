from django.db import models

class Order(models.Model):
    date_of_order = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()
    Total_price = models.DecimalField(max_digits=5,decimal_places=2)
    product_ID = models.IntegerField()

