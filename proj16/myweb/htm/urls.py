from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'htm.views.mainIndex', name='index'),
    url(r'^tag/$', 'htm.views.htmSearch', name='search'),
    url(r'^tag/add/$', 'htm.views.htmAdd', name='add'),
    url(r'^tag/update/$', 'htm.views.htmUpdate', name='update'),
    url(r'^tag/delete/$', 'htm.views.htmDelete', name='delete'),
    url(r'^tag/([a-z]+)/$', 'htm.views.htmTag', name='tag'),
    url(r'^calc/$', 'htm.views.htmCalc'),
]