from django.forms import ModelForm, DateInput

from .models import *


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'check_in_date',
            'check_out_date',
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
            'check_out_date': DateInput( 
                attrs={
                    'class':'form-control', 
                    'type':'date',
                    'placeholder': 'self.instance.check_out_date',
                }
            ),
        }
