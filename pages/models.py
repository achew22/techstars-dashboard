from django.db import models

class Page(models.Model):
	url = models.URLField()
	timeout = models.IntegerField()
	
	def __unicode__(self):
	    return "Page (for %s sec): %s" % (self.timeout, self.url)
