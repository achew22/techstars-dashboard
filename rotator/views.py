# https://bitbucket.org/twanschik/django-autoload/src/1698ab544030/autoload/middleware.py
from django.core.urlresolvers import reverse
from django.utils.importlib import import_module
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.utils import simplejson as json

from django.utils.importlib import import_module
from django.conf import settings

import logging
logging = logging.getLogger('techstars.rotator')

import settings

def index(request):
    return render_to_response("index.html")

def empty(request):
    return render_to_response("empty.html")
    
def leafs(request):
    response_data = []

    # Go through all installed apps looking for leaves
    for app in settings.INSTALLED_APPS:
        try:
            f = import_module("%s.leaves" % app).get_leaves
            logging.debug("Imported leaves for %s" % app)
        except (ImportError,AttributeError):
            f = lambda : []
        
        # By breaking this into its own section, we don't catch every error and
        # make it impossible to debug
        response_data += f()
        
    if response_data == []:
        response_data = [
            [reverse('rotator.views.empty'), 10 * 1000],
        ]

    return HttpResponse(json.dumps(response_data), mimetype="application/json")
