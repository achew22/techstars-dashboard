from pages.models import Page

import logging
logging = logging.getLogger('techstars.calendar.pages')

def get_leaves():
    to_return = []
    
    pages = Page.objects.all()
    
    for page in pages:
        to_return.append([page.url, page.timeout*1000])

    return to_return
