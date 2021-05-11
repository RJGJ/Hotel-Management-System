from django.db.models import Q, QuerySet

from .models import *

import datetime


def say_hello() -> str:
    '''just returns and prints hello'''
    print('hello from tasks.py')
    return 'hello from tasks.py'


def _make_unavailable() -> None:
    '''finds active reservations and makes 
    the corresponding rooms unavailable'''
    
    date_now = datetime.datetime.now().date()
    not_exp_reservations = Reservation.objects.filter(
        Q(claimed=True) & 
        Q(check_in_date__lte=date_now) & 
        Q(check_out_date__gte=date_now)
    )

    for reservation in not_exp_reservations:
        room = reservation.room
        if room.available :
            room.available = False
            room.save()
    pass


def _make_available():
    '''finds active reservations that are expired 
    and makes the corresponding rooms available'''
    # find all unavailable rooms
    rooms: QuerySet = Room.objects.filter(available=False)
    
    room: Room
    for room in rooms:

        # get all active reservations that refers to this room
        date_now: datetime.date = datetime.datetime.now().date()
        reservations: QuerySet = Reservation.objects.filter(
            Q(room=room) &
            Q(check_out_date__lt=date_now)
        )

        # make the room available
        if reservations.count() <= 0:
            room.available = True
            room.save()
        
        for reservation in reservations:
            filtered_room: Room = reservation.room
            filtered_room.available = True
            filtered_room.save()


def update_rooms_state() -> None:
    _make_unavailable()
    _make_available()


def do_tasks():
    tasks = [
        update_rooms_state,
    ]

    for task in tasks:
        task()