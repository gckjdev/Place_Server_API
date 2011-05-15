'''
Created on 2011-4-12

@author: James
'''

from django.conf.urls.defaults import patterns, url
from place.api.views import place_list, place_info, post_info, place_posts, \
    post_replies

urlpatterns = patterns('',
    url(r'^$', place_list),
    url(r'^place/(?P<key>\w+)/$', place_info),
    url(r'^place/(?P<key>\w+)/posts/', place_posts),
    url(r'^post/(?P<key>\w+)/$', post_info),
    url(r'^post/(?P<key>\w+)/replies/', post_replies),
)
