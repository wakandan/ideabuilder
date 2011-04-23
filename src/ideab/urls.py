from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import logging 

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^ideabuilder/', include('ideabuilder.urls')),
    #(r'^ideabuilder/signup/$', 'ideabuilder.views.builder.user_signup', {}, 'user_signup')             
)

