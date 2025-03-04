from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm
from django.views.decorators.csrf import csrf_exempt

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/list.html', {'reservations': reservations})

def add_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()

    return render(request, 'reservations/add.html', {'form': form})

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    return redirect('reservation_list')

@csrf_exempt
def change_reservation_status(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in ["pending", "confirmed", "cancelled"]:
            reservation.status = new_status
            reservation.save()
    return redirect("reservation_list")