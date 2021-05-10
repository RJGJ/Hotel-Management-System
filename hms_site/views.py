from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.serializers import json

from .forms import *
from .models import *


# Create your views here.
@login_required
def index(request):
    form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'hms_site/index.html', context)


@login_required
def available_rooms(request):
	
	# get rooms with state of 0 (vacant)
	rooms = Room.objects.filter(state=0)
	json_serializer = json.Serializer()
	rooms_serialized = json_serializer.serialize(rooms)

	print(rooms_serialized)

	data = {
		'message': 'hello world',
		'rooms': rooms,
	}
	return JsonResponse(data)
