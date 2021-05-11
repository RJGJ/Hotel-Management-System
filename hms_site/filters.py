import django_filters

from .models import *


class ReservationFilter(django_filters.FilterSet):
    class Meta:
        model = Reservation
        fields = '__all__'


class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['price',]
