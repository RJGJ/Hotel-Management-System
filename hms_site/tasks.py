from django.db.models import Q

from .models import *

import datetime


def say_hello():
    print('hello from tasks.py')


def update_rooms_state():

    # set rooms to occupied
    # get reservations that are not expired
    date_now = datetime.datetime.now().date()
    not_exp_reservations = Reservation.objects.filter(
        Q(claimed=True) & 
        Q(check_in_date__lte=date_now & 
        Q(check_out_date__gte=date_now))
    )

    for reservation in not_exp_reservations:
        print(reservation)
        room = reservation.room
        print(room.available)
        # if room.available == 0:
        #     print(room)



    # print('#########################################################')
    # print(Reservation.objects.all())
    # print(not_exp_reservations)


def do_tasks():
    tasks = [
        update_rooms_state,
    ]

    for task in tasks:
        task()