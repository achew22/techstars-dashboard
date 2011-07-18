from django.http import HttpResponse
from django.shortcuts import render

from countdown.models import Countdown

import logging
logging = logging.getLogger('techstars.countdown.views')

def view(request, id):
    event = Countdown.objects.get(id=id)
    return render(request, "countdown/index.html", {
        'event': event,
    })
