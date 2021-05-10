from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Room(models.Model):

    states = [
        (0, 'vacant'),
        (1, 'occupied'),
        (2, 'for cleaning'),
    ]

    name = models.CharField(max_length=255, blank=False, default=None)
    price = models.IntegerField()   # cost of stay per day
    state = models.IntegerField(choices=states)

    def __str__(self):
        return self.name


class Custumer(models.Model):
    first_name = models.CharField(max_length=255, blank=False, default=None)
    first_name = models.CharField(max_length=255, blank=False, default=None)
    email = models.EmailField(blank=True, default=None)
    number = PhoneNumberField(blank=False, default=None)

    def __str__(self):
        return self.first_name


class Reservation(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # the employee/admin that created this reservation
    creation_date = models.DateTimeField(auto_now=True)
    check_in_date = models.DateField(blank=False, default=None) # can be claimed within the day of target date
    claimed = models.BooleanField(default=False) # if reservation is claimed
    days = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255, blank=False, default=None)

    def __str__(self):
        return f'reservation on: {self.check_in_date}'
