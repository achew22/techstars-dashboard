from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('countdown.views',
    url(r'(?P<id>\d+)/$', 'view'),
)
