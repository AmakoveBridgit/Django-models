from django.contrib import admin

from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("Firstname","Secondname", "Emailaddress","password" ,"phoneNumber", "customerID")
admin.site.register(Customer,CustomerAdmin)




