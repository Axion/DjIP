# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('djip.views',
    url(r'^$', 'browse', name="djip_browse"),
    url(r'^djip_update_all/$', 'update_all', name='djip_update_all'),
)