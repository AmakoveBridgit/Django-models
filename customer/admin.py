from django.contrib import admin

from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname", "emailaddress","password" ,"phonenumber", "customerID")
admin.site.register(Customer,CustomerAdmin)




