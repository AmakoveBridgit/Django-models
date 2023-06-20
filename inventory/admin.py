from django.contrib import admin

from .models import Product
class ProductAdmin(admin .ModelAdmin):
    list_display = ('name','price','image','date_created','stock','date_updated')
admin.site.register(Product,ProductAdmin)
