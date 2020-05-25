from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'vote.views.voteIndex'),
    url(r'^insert/$', 'vote.views.voteInsert'),
    url(r'^update/$', 'vote.views.voteUpdate'),
    url(r'^delete/$', 'vote.views.voteDelete'),
    url(r'^check/([0-9]+)$', 'vote.views.voteCheck'),
    url(r'^confirm/([0-9]+)$', 'vote.views.voteConfirm'),
# name='index'
# name='insert'
# name='update'
# name='delete'
# name='check'
# name='confirm'


]