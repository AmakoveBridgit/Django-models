# from .forms import ProductCartForm
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Cart

# def product_upload_view(request):
#     form = ProductCartForm()
    
    
#     return render(request,"cart/product_get.html",{"form": form})

# # ..........................
# def add_to_cart(request):
#     if request.method == 'POST':
#         form = ProductCartForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cart_list')
#     else:
#         form = ProductCartForm()
#     return render(request, 'cart/add_to_cart.html', {'form': form})

# def remove_cart_item(request, cart_item_id):
#     cart_item = get_object_or_404(Cart, pk=cart_item_id)
#     if request.method == 'POST':
#         form = ProductCartForm(request.POST, instance=cart_item)
#         if form.is_valid():
#             form.save()
#             return redirect('cart_list')
#     else:
#         form = ProductCartForm(instance=cart_item)
#     return render(request, 'cart/edit_cart_item.html', {'form': form, 'cart_item': cart_item})

# def cart_list(request):
#     cart_items = Cart.objects.all()
#     return render(request, 'cart/cart_list.html', {'cart_items': cart_items})


# ......................................

from django.shortcuts import render, redirect
from .models import Cart
from datetime import datetime
from .models import Product
def view_cart(request):
    product_cart = Cart.objects.all()
    total_cart_price = 0
    for item in product_cart:
        item.total_price = item.price * item.quantity
        total_cart_price += item.total_price
    return render(request, "cart/view_cart.html", {"product_cart": product_cart, "total_cart_price": total_cart_price})
def update_cart(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = Cart.objects.get(id=id)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')
def remove_item(request, id):
    cart_item = Cart.objects.get(id=id)
    cart_item.delete()
    return redirect('view_cart')
def empty_cart(request):
    Cart.objects.all().delete()
    return redirect("view_cart")
def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart_item = Cart (
        name = product.name,
        price = product.price,
        image = product.image,
        quantity = 1,
        date_added=datetime.now(),
    )
    cart_item.save()
    return redirect("products_list_view")





