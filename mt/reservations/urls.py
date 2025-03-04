from django.urls import path
from .views import reservation_list, add_reservation, delete_reservation, change_reservation_status

urlpatterns = [
    path('', reservation_list, name='reservation_list'),
    path('add/', add_reservation, name='add_reservation'),
    path('delete/<int:reservation_id>/', delete_reservation, name='delete_reservation'), 
    path('change-status/<int:reservation_id>/', change_reservation_status, name='change_reservation_status'),
]