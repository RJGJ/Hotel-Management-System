from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.core.serializers import json
from django.contrib.admin.views.decorators import staff_member_required

from .forms import *
from .models import *
from .tables import *
from .filters import *
from .tasks import *


# Create your views here.
@login_required
@staff_member_required
def index(request, reservation_id=None):

    do_tasks()

    form = ReservationForm()

    should_update = False

    if not reservation_id == None:
        reservation_obj = Reservation.objects.get(id=reservation_id)
        form = ReservationForm(instance=reservation_obj)
        should_update = True

    if request.method == 'POST':
        
        form = ReservationForm(request.POST)
        
        if not reservation_id == None:
            reservation_obj = Reservation.objects.get(id=reservation_id)
            form = ReservationForm(request.POST, instance=reservation_obj)
        
        if form.is_valid:
            if should_update:
                obj = form.save(commit=False)
            else:
                obj = form.save()
                creator = request.user
                obj.creator = creator
            
            obj.save()

    context = {
        'form': form,
        'should_update': should_update
    }
    return render(request, 'hms_site/index.html', context)


@login_required
@staff_member_required
def available_rooms(request):

    do_tasks()
    
    # get rooms with state of 0 (vacant)
    rooms = Room.objects.filter(available=True)
    json_serializer = json.Serializer()
    rooms_serialized = json_serializer.serialize(rooms)

    data = {
        'message': 'hello world',
        'rooms': rooms_serialized,
    }
    
    return JsonResponse(data)


@login_required
@staff_member_required
def reservations(request):

    do_tasks()

    queryset = Reservation.objects.all()
    table = ReservationTable(queryset)

    my_filter = ReservationFilter(request.GET, queryset)
    queryset = my_filter.qs
    table = ReservationTable(queryset)

    context = {
        'table': table,
        'filter': my_filter,
    }
    return render(request, 'hms_site/reservations.html', context)
