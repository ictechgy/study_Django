#만든 views.py 파일

#함수명은 index로 만들기로 했었다.
#def index():
#    pass
#여기까지 하면 함수 못찾았다는 것은 안뜨지만 오류가 난다.

#함수에 인자 하나는 있어야 한다. request인자 꼭 필요

#def index(request):
#    pass
# Client에서는 HTTP Request를 하는데 인자를 서버에서는 모두 받아서 view로 보낸다. 어떠한 방식의 요청을 했는지 기본적으로는 받아줘야 한다.
#따라서 request 매개변수는 항상 필요하다. 이름은 꼭 저거일 필요는 없다.

#근데 또 오류가 난다. return이 없어서 오류. 서버가 request를 받고 결과를 처리한 뒤 response 응답을 안해줘서그럼


from django.http import HttpResponse
# Http 규격에 맞춘 전송을 위한 import.

def index(request):
    return HttpResponse('응답완료') #실질적으로 보내고자 하는 데이터를 서버에서 클라이언트로 보낸다.
#return은 꼭 해야하나? HttpResponse()자체가 그냥 서버에서 클라이언트로 메시지를 던지는 것 아닐까?






def blog(request): #클라이언트의 http request에 대해 뭘 요구하는 건지를 알아야하므로 쓰는 매개변수 request. 꼭 저 이름일 필요는 없다.
    return HttpResponse('블로그 패턴 응답 완료')
#이 함수는 ^blog/$' 패턴에만 응답하도록 되어있다.
#사용자가 127.0.0.1:8000/blog 라고 들어가면 사용되는 함수이다. 만약 path를 blug 이런식으로 쓰면 안됨
#그냥 127.0.0.1:8000/ 라고만 치면 '^$' 패턴에 대한 것임

#만약 blog라는 path뿐만이 아닌 여러 path에 대해서도 어떤 함수를 동작시키고자 한다면 정규표현식으로 패턴을 나타내주면 된다.



#4. slug패턴 받은 것에 대해 선생님은 아래와 같이 함수를 구성하심
def viewOfPage(request, slug):
    res=' '.join(slug.split('-'))
    return HttpResponse('{}'.format(res))
#.split 및 .join 함수에 대한 것 -> https://wikidocs.net/13 참고

#split은 문자열에 특정 문자가 포함되어있다면 그것들을 구분자로 삼아 제거하면서 리스트 요소로 만듬
#join은 .온점 앞에 있는 문자(변수라면 변수의 실질적문자값)를 괄호 안에 있는 문자열에 있어서 문자단위 하나하나 사이에 집어넣는다.

#이렇게 path정보를 함수로 보내고 그 path를 활용할 수 있다. 당연히 path에 따라 결과를 세분화 할 수도 있을 것이다.