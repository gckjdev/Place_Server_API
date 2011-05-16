'''
Created on 2011-4-12

@author: James
'''

from django.conf.urls.defaults import patterns, url
from place.api.views import internal_method

urlpatterns = patterns('',
    url(r'^i/', internal_method),
)
