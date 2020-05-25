from django.conf.urls import url

urlpatterns = [

    url(r'^$', 'htm.views.mainIndex'),
    url(r'^tag/$', 'htm.views.htmTag'),


]