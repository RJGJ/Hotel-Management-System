from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import *


# Create your views here.
@login_required
def index(request):
    form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'hms_site/index.html', context)
