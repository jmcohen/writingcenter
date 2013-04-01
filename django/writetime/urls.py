from django.conf.urls import patterns, include, url
import list.views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'list.views.index'),
    url(r'^offer$', 'list.views.offer'),
    url(r'^accept/(\d*)$', 'list.views.accept'),
    url(r'^submitOffer/$', 'list.views.submitOffer'),
    url(r'^submitAccept/(\d*)$', 'list.views.submitAccept'),
    url(r'^submitRemove/(\d*)$', 'list.views.submitRemove'),
    url(r'^verify$', 'list.views.verify'),
    # Examples:
    # url(r'^$', 'writetime.views.home', name='home'),
    # url(r'^writetime/', include('writetime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
