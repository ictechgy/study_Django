from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'myweb.views.index', name='index'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^htm/', include('htm.urls', namespace='htm')),
    url(r'^vote/', include('vote.urls', namespace='vote')),
    # 1990 ~ 1999, 2000 ~ 2999
    url(r'^(?:199[0-9]|2[0-9]{3})/$', 'myweb.views.viewOfYear'),
    # 01 ~ 09, 10 ~ 12
    url(r'^month/(?:0[1-9]|1[0-2])/$', 'myweb.views.viewOfMonth'),
    # 1 ~ 9, 10 ~ 29, 30, 31
    url(r'^day/(?:[1-9]|[1-2][0-9]|30|31)/$', 'myweb.views.viewOfDay'),
    url(r'^admin/', include(admin.site.urls)),
    # 슬러그 패턴
    url(r'^((?:[a-z]+-?)+)/$', 'myweb.views.viewOfPage'),
]
