from django.http import HttpResponseRedirect

from pages.models import Page

def view(request,id):
    page = Page.objects.get(id=id)
    return HttpResponseRedirect(page.url)
