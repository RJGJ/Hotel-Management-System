from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('reservation/<int:reservation_id>/', index, name='reservation'),
    path('reservations', reservations, name='reservations'),
]

urlpatterns += [
	path('api/available-rooms/', available_rooms, name='available_rooms'),
]
