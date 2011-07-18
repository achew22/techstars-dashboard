from django.db import models
from django.core.urlresolvers import reverse

class Countdown(models.Model):
    title = models.CharField(max_length=255)    
    date = models.DateTimeField()
    timeout = models.IntegerField()
    
    def __unicode__(self):
        return "%s @ %s" % (self.title, self.date)
        
    def get_absolute_url(self):
        return reverse('countdown.views.view', kwargs = {'id' : self.id})
