from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'vote.views.voteIndex', name='index'),
    url(r'^insert/$', 'vote.views.voteInsert', name='insert'),
    url(r'^update/$', 'vote.views.voteUpdate', name='update'),
    url(r'^delete/$', 'vote.views.voteDelete', name='delete'),
    url(r'^check/([0-9]+)$', 'vote.views.voteCheck', name='check'),
    url(r'^confirm/([0-9]+)$', 'vote.views.voteConfirm', name='confirm'),



]