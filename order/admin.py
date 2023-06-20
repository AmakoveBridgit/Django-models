from django.contrib import admin

from .models import Order
class OrderAdmin(admin .ModelAdmin):
    list_display = ('date_of_order','quantity','Total_price','product_ID')
admin.site.register(Order,OrderAdmin)







   
