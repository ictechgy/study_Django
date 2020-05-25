from django.conf.urls import url

urlpatterns = [
    url(r'^(?:199[0-9]|2[0-9]{3})/$', 'blog.views.viewOfYear'),
    url(r'^month/(?:0[1-9]|1[0-2])/$', 'blog.views.viewOfMonth'),
    url(r'^day/(?:[1-9]|[1-2][0-9]|30|31)/$', 'blog.views.viewOfDay'),
    url(r'^(?:(?:[a-z]+-?)+)/$', 'blog.views.viewOfPage'),
]