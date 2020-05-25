from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'board.views.boardIndex', name='index'),
    url(r'^insert/$', 'board.views.boardInsert', name='insert'),
    url(r'^update/$', 'board.views.boardUpdate', name='update'),
    url(r'^delete/$', 'board.views.boardDelete', name='delete'),
    url(r'^view/([0-9]+)/$', 'board.views.boardView', name='view'),
    url(r'^goodbad/([0-9]+)/$', 'board.views.boardGoodBad', name='goodbad'),
    url(r'^comment/add/$', 'board.views.boardCommentAdd', name='comment_add'),
    url(r'^comment/delete/$', 'board.views.boardCommentDelete', name='comment_delete'),
]