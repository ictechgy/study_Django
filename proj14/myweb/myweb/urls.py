from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^account/', include('django.contrib.auth.urls')),#namespace 쓸 필요 없음. 장고 기본 기능 사용할 것
    #로그인과 로그아웃처리를 위한 url패턴. 로그인과 로그아웃처리를 우리가 할 필요가 없음
    url(r'^account/join/$', 'myweb.views.join', name='join'),
    #계정 생성 및 수정에 대해서 우리가 신경을 써줘야 한다.

    #이렇게만 하면 웹페이지에서 /account/login/ 및 {% url 'login' %} 을 들어가면 login.html 파일로 연결이 된다.
    #/account/logout/ 또는 {% url 'logout' %}을 하면 로그아웃이 자동으로 이루어지고 logged_out.html 파일로 연결이 된다.

    #로그인과 로그아웃에 대한 페이지는 전체 프로젝트에 대해서 적용을 시킬 것이므로 바깥 template쪽에다 두는 것임
    #전체적인 관리가 필요한 것들은 바깥 template에다가 두고 앱별 따로 관리할 것들은 각 app 하위의 templates에다가 보관





    url(r'^$', 'myweb.views.index', name='index'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^htm/', include('htm.urls', namespace='htm')),
    url(r'^vote/', include('vote.urls', namespace='vote')),
    # 1990 ~ 1999, 2000 ~ 2999
    url(r'^(?:199[0-9]|2[0-9]{3})/$', 'myweb.views.viewOfYear'),
    # 01 ~ 09, 10 ~ 12
    url(r'^month/(?:0[1-9]|1[0-2])/$', 'myweb.views.viewOfMonth'),
    # 1 ~ 9, 10 ~ 29, 30, 31
    url(r'^day/(?:[1-9]|[1-2][0-9]|30|31)/$', 'myweb.views.viewOfDay'),
    url(r'^admin/', include(admin.site.urls)),
    # 슬러그 패턴
    url(r'^((?:[a-z]+-?)+)/$', 'myweb.views.viewOfPage'),
]
