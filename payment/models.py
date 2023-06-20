from django.db import models

class Payment(models.Model):
    payment_id = models.IntegerField()
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)
    customer_id = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)
