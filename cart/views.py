from django.shortcuts import render
from .forms import ProductCartForm

def product_upload_view(request):
    form = ProductCartForm()
    
    
    return render(request,"cart/product_get.html",{"form": form})

