from django.conf.urls import include, url  #include 함수와 url 함수를 쓰기 위함?
from django.contrib import admin #admin쪽을 위한 import?

urlpatterns = [
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #기본으로 존재하는 패턴

    url(r'^$', 'myweb.views.index', name='index'),
    # include 함수를 안쓸 것이라면 패턴의 끝을 나타내는 $필수
    # 정규표현식 패턴에 매치되는 path정보에 대해서, myweb 앱 안의 views라는 스크립트파일 안의 index 함수를 호출해라
    # 호출하는 함수가 실제로도 존재해야한다. 함수가 존재하지 않으면 저 url을 이용해 접근했을 시 오류
    # 가급적이면 시크릿모드로 창을 열자 - 왜?
    # http://127.0.0.1:8000/ 를 연다면 위의 두번째 패턴에 해당하는 것임.
    # 근데 뒤의 views가 myweb 안에 없어서 안열린다. 해당하는 것을 못찾았다고 뜸

    # http://127.0.0.1:8000/b 를 쳤을 때 page not found 뜸. 이는 /b/에 해당하는 패턴이 존재하지 않아서 안뜨는 것
    url(r'^b/$', 'myweb.views.index'), #이거 하면 패턴일치하는건 찾긴 해서 page not found는 안뜨는데, views가 역시나 없어서..
    
    #index 함수를 만들어보자
    #현재 myweb 안에는 views.py가 없으니 새로 만들자. 
]
