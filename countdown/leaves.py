from countdown.models import Countdown

import logging
logging = logging.getLogger('techstars.countdown.leaves')

def get_leaves():
    to_return = []
    
    countdowns = Countdown.objects.all()
    
    for countdown in countdowns:
        to_return.append([countdown.get_absolute_url(), countdown.timeout*1000])

    return to_return
