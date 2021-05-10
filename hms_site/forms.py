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
            'check_in_date': DateInput( 
                attrs={
                    'class':'form-control', 
                    'type':'date',
                    'placeholder': 'self.instance.check_in_date',
                }
            ),
        }
