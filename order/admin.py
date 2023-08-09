from django.contrib import admin

from .models import Order
class OrderAdmin(admin .ModelAdmin):
    list_display = ('customer','cart','date_of_order','quantity','total_price')
admin.site.register(Order,OrderAdmin)







   
