from django.contrib import admin
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class RoomAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'available')
    list_filter = ('available', 'id', 'name', 'available')
    search_fields = ('name',)


class CustumerAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'email', 'number')
    list_filter = ('id', 'first_name', 'email', 'number')


class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'creator',
        'creation_date',
        'check_in_date',
        'check_out_date',
        'claimed',
        'room',
        'customer_name',
    )
    list_filter = (
        'creator',
        'creation_date',
        'check_in_date',
        'check_out_date',
        'claimed',
        'room',
        'id',
        'creator',
        'creation_date',
        'check_in_date',
        'check_out_date',
        'claimed',
        'room',
        'customer_name',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Room, RoomAdmin)
_register(models.Custumer, CustumerAdmin)
_register(models.Reservation, ReservationAdmin)
