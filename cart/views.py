from .forms import ProductCartForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart

def product_upload_view(request):
    form = ProductCartForm()
    
    
    return render(request,"cart/product_get.html",{"form": form})

# ..........................
def add_to_cart(request):
    if request.method == 'POST':
        form = ProductCartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = ProductCartForm()
    return render(request, 'cart/add_to_cart.html', {'form': form})

def remove_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id)
    if request.method == 'POST':
        form = ProductCartForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = ProductCartForm(instance=cart_item)
    return render(request, 'cart/edit_cart_item.html', {'form': form, 'cart_item': cart_item})

def cart_list(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'cart_items': cart_items})

