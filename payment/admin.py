from django.contrib import admin

from.models import Payment
class Payment_admin(admin.ModelAdmin):
    list_display=("payment_id","customer_id","payment_amount","payment_date")
admin.site.register(Payment,Payment_admin)












