from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += [
	path('api/available-rooms/', available_rooms, name='available_rooms'),
]
