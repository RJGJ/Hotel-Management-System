from .models import *


def say_hello():
    print('hello from tasks.py')


def update_rooms_state():

    # set rooms to occupied
    # get reservations that are not expired
    # Reservation.objects.filter(check_in_date)
    pass


def do_tasks():
    tasks = [
        say_hello,
    ]

    for task in tasks:
        task()