from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #2018-06-25
    url(r'^vote/', include('vote.urls', namespace='vote')),
    
    
    
    
    
    
    
    
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^htm/', include('htm.urls')),
    
    
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myweb.views.index', name='index'),
    # include 함수를 안쓸 것이라면 패턴의 끝을 나타내는 $필수
    # 정규표현식 패턴에 매치되는 path정보에 대해서, myweb 앱 안의 views라는 스크립트파일 안의 index 함수를 호출해라
    # 호출하는 함수가 실제로도 존재해야한다. 함수가 존재하지 않으면 저 url을 이용해 접근했을 시 오류
    # 가급적이면 시크릿모드로 창을 열자 - 왜?
    # http://127.0.0.1:8000/ 를 연다면 위의 두번째 패턴에 해당하는 것임.
    # 근데 뒤의 view가 없어서 안열린다.
    # http://127.0.0.1:8000/b 를 쳤을 때 page not found 뜸. 이는 /b/에 해당하는 패턴이 존재하지 않아서 안뜨는 것
    url(r'^b/$', 'myweb.views.index'), #이거 하면 패턴일치하는건 찾긴 해서 page not found는 안뜨는데, view가 역시나 없어서..
    
    #함수를 만들어보자




    url(r'^blog/$', 'myweb.views.blog', name='blog'),
    #blog라는 path패턴으로 접속한 것에 대해 연결시켜 줄 것이 뒤에 있다.
    #myweb이라는 app 안의 views라는 스크립트. 그리고 그 안의 blog라는 함수
    #include함수를 쓰지 않았기에 정규표현식 마지막에는 $가 들어간다. 
    #include를 쓰는 것은 받은 url패턴에 대해 다른 app속의 urls.py로 넘겨주고자 할 때 쓰는 것 같다.
    #name 을 쓰는 것은 나중에. name을 쓰면 편리한 기능이 있다고 한다.


    #문제
    #1. 1990 ~ 2999 까지의 정규 표현식을 사용하여 myWeb의 viewOfYear 함수로 연결하시오.
    url(r'^(199|2[0-9]{2})[0-9]$', 'myweb.views.viewOfYear'),
    #2. 01 ~ 12 까지의 정규 표현식을 사용하여 myWeb의 viewOfMonth 함수로 연결하시오.
    url(r'^(0[1-9]|1[0-2])$', 'myweb.views.viewOfMonth'),
    #3. 1 ~ 31 까지의 정규 표현식을 사용하여 myWeb의 viewOfDay 함수로 연결하시오.
    url(r'^([1-9]|[1-2][0-9]|3[0-1])$', 'myweb.views.viewOfDay'),
    #4. -가 단어와 단어 사이에 포함되는 정규 표현식을 사용하여 myWeb의 viewOfPage 함수로 연결하시오.
    #예) python-django 또는 django-url-pattern 또는 python -> 이런 것을 슬러그(slug)패턴이라고 한다.
    url(r'^([a-z]+-?)+$', 'myweb.views.viewOfPage'),

    
    #선생님 답
    #1. [0-9]{4}라고 할 수도 있겠지만... 1990~1999, 2000 ~ 2999 패턴으로 분리
    url(r'^(199[0-9]|2[0-9]{3})/$', 'myweb.views.viewOfYear'),
    #문제는 이렇게 한 경우 연도값이 함수의 인자로 넘어간다. 혹여나 함수에 매개변수 request만 있다고 한다면
    #사용자의 request를 받지 못하고 request로 연도값이 넘어간다. 따라서 우리는 선택지 두개 중 하나를 선택해야한다.
    #함수에 매개변수 하나를 더 받도록 만들던지, 아니면 여기 패턴에서 인자로 넘기지 않도록 ?:을 추가적으로 써주던지

    #2. 01~09와 10~12를 분리
    url(r'^(?:0[1-9]|1[0-2])/$','myweb.views.viewOfMonth'),

    #3. 1~9, 10~29, 30,31 분리
    url(r'^(?:[1-9]|[1-2][0-9]|30|31)/$','myweb.views.viewOfDay'),

    #문제는 이렇게 하는 경우 path에 10~12를 입력하거나 하면 월에 매치가 된다.
    #이 패턴은 리스트인데 순서대로 값 검증을 한다. 그러다가 10이라는 path를 만나면 월패턴으로 먼저 인식한다.
    #따라서 구분할 수 있는 구분자 패턴을 먼저 넣어줘야 한다.
    #선생님은 그래서 패턴에다가 ^month/ 와 ^day/ 라는 패턴을 추가적으로 넣어주셨다.
    #위와 같이 하면 이제 패턴에 /month/12 와 /day/12는 구분이 되게 된다.

    #4. slug pattern
    url(r'^(?:[a-z]+-?)+/$','myweb.views.viewOfPage'),
    #마지막에 슬래시 빠지면 패턴인식을 못하네
    #만약 이 패턴을 함수로 전달하고자 한다면 r'^((?:[a-z]+-?)+)/$'로 만들어줘야 한다.
    # r'^([a-z]+-?)+/$' 라고 한다면 인자로 여러값이 넘어갈 수도 있을 듯

    #또 이렇게 되면 admin 패턴이 인식이 안된다. admin에 접근 안할 것이면 상관 없지만 admin패턴에 접속하고자 한다면
    #admin 패턴을 slug위로 올리도록 한다. 가급적 slug패턴은 맨 아래에 두는 것이 좋다


    #만약 (?P<name>'패턴') 형식으로 만든다면, 키워드인자방식인데 함수에서 매개변수에 동일 키워드가 있으면 그 곳으로 
    #넘어가고 그렇지 않으면 위치인자방식으로 맨 첫부분에 들어가게 되는건가? 
    #함수에 a,b라는 매개변수가 존재한다면 a에는 무조건 request값이 전달되는건가? b에는 path에서 넘어온 값이 들어가고?
    #함수에는 위치매개변수 두개가 존재하는데 request는 언제나 넘어오겠지만 path에서 인자를 안넘겨주면 오류뜨려나
    #가변인자로 존재한다면 넘겨줘도 되고 안넘겨도 되고. 안넘기면 기본값 쓸테고

    #함수에 인자로서 전달해야 하는 경우라면 전달을 하면 되고 전달할 필요가 없다면 전달하지 않아도 된다.



    #계층화 패턴
    url(r'^blog/', include('blog.urls')),
    #달러기호는 패턴의 끝인데 여기서 패턴이 끝인게 아니라 패턴은 저 blog.urls에 더 있다. 라는 의미를 위해 $를 뺀다
    #사실 이 패턴은 slug패턴 위에 있어야 될 것
    #위에 보면 blog패턴이 이미 있긴 함. 저거랑 중복되니 하나 없애야 함


]
