from django.conf.urls import url

urlpatterns = [

    url(r'^$', 'htm.views.mainIndex'),
    url(r'^tag/$', 'htm.views.htmTag'),
    url(r'^tag/([a-z]+)/$', 'htm.views.htmAdd'),

]