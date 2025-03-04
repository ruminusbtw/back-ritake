from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'date', 'status']
