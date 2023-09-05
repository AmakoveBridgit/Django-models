from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment/upload/', views.payment_upload_view, name='payment_upload_view'),
    path('payment/list/', views.payment_list, name='payment_list_view'),
    path('payment/detail/<int:id>/', views.payment_detail, name='payment_detail_view'),
    path('payment/update/<int:id>/', views.payment_update_view, name='payment_update_view'),
    path('payment/delete/<int:id>/', views.delete_payment, name='delete_payment_view'),
]