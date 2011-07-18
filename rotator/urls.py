from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'rotator.views.index'),
    url(r'^empty', 'rotator.views.empty'),
    url(r'^leafs', 'rotator.views.leafs'),
)
