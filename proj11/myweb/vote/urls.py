from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'vote.views.voteIndex'),
    url(r'^insert/$', 'vote.views.voteInsert'),
    url(r'^update/$', 'vote.views.voteUpdate'),
    url(r'^delete/$', 'vote.views.voteDelete'),
    url(r'^check/([0-9]+)/$', 'vote.views.voteCheck'),
    url(r'^confirm/([0-9]+)/$', 'vote.views.voteConfirm'),
# name='index'
# name='insert'
# name='update'
# name='delete'
# name='check'
# name='confirm'

#왜 가끔 name이나 namespace 설정시 오류뜨는거지.. 다른부분에서 오류가 나는건가
#그리고 url 패턴 끝에 항상 슬래시 붙여주는데 이는 다음 urls.py에서 /로 시작함으로서 안붙여도 되는거 아닐까
#붙이는거 자체는 urls.py마다 처리할 path를 달리 해주도록 하기 위해서?인거같긴 한데..어떤 구분의 역할.
]