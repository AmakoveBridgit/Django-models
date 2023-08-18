from django.urls import path
from .views import product_upload_view
from .views import cart_list
from .views import add_to_cart
from .views import remove_cart_item
# from.import views


urlpatterns= [
    path("products/get/", product_upload_view,
       name="product_get_view"),



# ....................

    path('cart/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_list, name='cart_list'),
    path('cart/remove/<int:cart_item_id>/', remove_cart_item, name='remove_cart_item'),

]