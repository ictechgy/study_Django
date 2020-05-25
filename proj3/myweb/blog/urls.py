from django.conf.urls import url

urlpatterns = [
    url(r'^(?:199[0-9]|2[0-9]{3})/$', 'blog.views.viewOfYear'),

    url(r'^month/(?:0[1-9]|1[0-2])/$','blog.views.viewOfMonth'),

    url(r'^day/(?:[1-9]|[1-2][0-9]|30|31)/$','blog.views.viewOfDay'),

    url(r'^(?:[a-z]+-?)+/$','blog.views.viewOfPage'),
    url(r'^(?:(?:[a-z]+-?))+/$','blog.views.viewOfPage'), #선생님의 패턴방식. 동일하지 않나 뭐..

    #/blog/admin 블로그쪽에 대한 어드민은 존재하지 않는 상태
]