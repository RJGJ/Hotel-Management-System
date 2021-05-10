from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class RoomAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'state')
    list_filter = ('id', 'name', 'price', 'state')
    search_fields = ('name',)


class CustumerAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'email', 'number')
    list_filter = ('id', 'first_name', 'email', 'number')


class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'creator',
        'creation_date',
        'target_date',
        'claimed',
        'days',
        'room',
        'custumer',
    )
    list_filter = (
        'creator',
        'creation_date',
        'target_date',
        'claimed',
        'room',
        'custumer',
        'id',
        'creator',
        'creation_date',
        'target_date',
        'claimed',
        'days',
        'room',
        'custumer',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Room, RoomAdmin)
_register(models.Custumer, CustumerAdmin)
_register(models.Reservation, ReservationAdmin)
