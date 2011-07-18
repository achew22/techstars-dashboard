from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('goog_calendar.views',
    url(r'(?P<id>\d+)/$', 'view'),
)
