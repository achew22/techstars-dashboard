from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # For static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Homepage (rotator)
    url(r'^$', 'rotator.views.index'),

    url(r'^rotator/', include('rotator.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += staticfiles_urlpatterns() # Serve static in development 
