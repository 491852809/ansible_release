from django.conf.urls import patterns, url, include

from .views import *

servers_urls = patterns('',
        url(r'^$',Servers_InfoList.as_view(),name='servers_info-list'),
        url(r'^/(?P<eth1>.+)$',Servers_InfoDetail.as_view(),name='servers_info-detail'),
        )

test_urls = patterns('',
        url(r'^$',Test.as_view(),name='test-list'),
        )

urlpatterns = patterns('',
        url(r'^base_info',include(servers_urls)),
        url(r'^test',include(test_urls)),
        )
