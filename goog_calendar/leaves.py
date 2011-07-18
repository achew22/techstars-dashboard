from goog_calendar.models import Calendar

import logging
logging = logging.getLogger('techstars.calendar.leaves')

def get_leaves():
    to_return = []
    
    calendars = Calendar.objects.all()
    
    for calendar in calendars:
        to_return.append(calendar.get_absolute_url())

    return to_return
