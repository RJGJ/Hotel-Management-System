from django.forms import ModelForm, DateInput

from .models import *


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'check_in_date',
            'days',
            'room',
            'customer_name',
            'claimed',
        ]
        widgets = {
            'target_date': DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
