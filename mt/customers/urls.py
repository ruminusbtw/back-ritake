from django.urls import path
from .views import customer_list, create_customer

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('create/', create_customer, name='create_customer'),
]
