from django.forms import ModelForm

from .models import *


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'target_date',
            'days',
            'room',
        ]
