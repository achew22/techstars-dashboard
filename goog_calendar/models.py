from django.db import models
from django.core.urlresolvers import reverse

class Calendar(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    timeout = models.IntegerField()
    
    def __unicode__(self):
        return "Calendar: %s" % (self.title)
        
    def get_absolute_url(self):
        return reverse('goog_calendar.views.view', kwargs = {'id' : self.id})
