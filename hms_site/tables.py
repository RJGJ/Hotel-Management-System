import django_tables2 as tables

from .models import *


class ReservationTable(tables.Table):
    id = tables.LinkColumn('reservation', args=[tables.A('id')])
    class Meta:
        model = Reservation
