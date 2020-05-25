from django.conf.urls import include, url
from django.contrib import admin


from django.conf.urls.static import static
from django.conf import settings
#파일 업로드기능 쓰려면 업로드에 대한 url패턴이 필요하고 파일에 대해 접근을 할때에도 패턴이 필요한데 이에 대해 자동생성 이용

urlpatterns = [
    url(r'^redactor/', include('redactor.urls')), #namespace 추가하지 말 것. 이는 account에 대한 것처럼 장고 기본기능 쓰는 것임
    #그리고 맨 밑에 세팅 추가



    url(r'^board/', include('board.urls', namespace='board')),

    

    url(r'^$', 'myweb.views.index', name='index'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^htm/', include('htm.urls', namespace='htm')),
    url(r'^vote/', include('vote.urls', namespace='vote')),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^account/join/$', 'myweb.views.join', name='join'),
    # 1990 ~ 1999, 2000 ~ 2999
    url(r'^(?:199[0-9]|2[0-9]{3})/$', 'myweb.views.viewOfYear'),
    # 01 ~ 09, 10 ~ 12
    url(r'^month/(?:0[1-9]|1[0-2])/$', 'myweb.views.viewOfMonth'),
    # 1 ~ 9, 10 ~ 29, 30, 31
    url(r'^day/(?:[1-9]|[1-2][0-9]|30|31)/$', 'myweb.views.viewOfDay'),
    url(r'^admin/', include(admin.site.urls)),
    # 슬러그 패턴
    #url(r'^((?:[a-z]+-?)+)/$', 'myweb.views.viewOfPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #settings.py에서 추가한 것에 대한 부분
