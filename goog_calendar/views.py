from datetime import datetime
from lxml import etree

from django.http import HttpResponse
from django.shortcuts import render
from goog_calendar.models import Calendar

import logging
logging = logging.getLogger('techstars.goog_calendar.views')

def extract_text(tree, xpath):
    tree.xpath(xpath,  
        namespaces = {
            'atom':'http://www.w3.org/2005/Atom'
        }
    )

def view(request,id):
    calendar = Calendar.objects.get(id=id)

    tree = etree.parse(calendar.url)

    #Unlike the rest of the world. Xpath, [1] is the first
    title = tree.xpath("/atom:feed/atom:entry[1]/atom:title/text()",
        namespaces = {
            'atom': 'http://www.w3.org/2005/Atom',
        }
    )[0]

    summary = tree.xpath("/atom:feed/atom:entry[1]/atom:summary/text()",
        namespaces = {
            'atom': 'http://www.w3.org/2005/Atom',
        }
    )[0]
    
    # Had issues with &nbsp; in the summary. Kill it
    summary = summary.replace('&nbsp;', '')
    
    # The actual event date is held in text so try to extract it via str manip
    date = summary[10:summary.find("<br>")] 
    #logging.debug("Date:"+date)

    # Now clean up the summary
    summary = summary[10+len(date):]
    logging.debug(summary)
    
    event = {
        'title':title,
        'date': date,
        'summary':summary,
    }

    #return HttpResponse("")

    return render(request, "calendar/index.html", {
        'calendar': calendar,
        'event': event,
    })
