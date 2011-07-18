from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # For static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Homepage (rotator)
    url(r'^$', 'rotator.views.index'),

    url(r'^rotator/', include('rotator.urls')),
    url(r'^calendar/', include('goog_calendar.urls')),
    url(r'^countdown/', include('countdown.urls')),

    # Comment the next line to disable the admin:
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += staticfiles_urlpatterns() # Serve static in development 
