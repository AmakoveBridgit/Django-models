from django.urls import path
from .views import product_upload_view


urlpatterns= [
    path("products/get/", product_upload_view,
       name="product_get_view"),
]

