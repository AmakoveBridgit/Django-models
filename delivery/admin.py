from django.contrib import admin

# Register your models here.

from .models import Delivery
# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    list_display=("name", "address", "phoneNumber", "deliverytime","isdelivered")
admin.site.register(Delivery,DeliveryAdmin)