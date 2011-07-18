from django.db import models

class Page(models.Model):
	url = models.URLField()
	timeout = models.IntegerField()
