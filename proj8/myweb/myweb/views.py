#만든 view.py 파일

#함수명은 index로 만들기로 했었다.
#def index():
#    pass
#여기까지 하면 함수 못찾았다는 것은 안뜨지만 오류가 난다.

#함수에 인자 하나는 있어야 한다. request인자 꼭 필요

#def index(request):
#    pass
# Client에서는 HTTP Request를 하는데 인자를 서버에서는 모두 받아서 view로 보낸다. 아무튼 페이지에 대한 요청을 받기 위해 request필요

#근데 또 오류가 난다. return이 없어서 오류. 서버가 request를 받고 결과를 처리한 뒤 response 응답을 안해줘서그럼


from django.http import HttpResponse
# Http 규격에 맞춘 전송을 위한 import.

#def index(request):
#    return HttpResponse('응답완료') #실질적으로 보내고자 하는 데이터를 서버에서 클라이언트로 보낸다.







def blog(request): #클라이언트의 http request에 대해 뭘 요구하는 건지를 알아야하므로 쓰는 매개변수 request. 꼭 저 이름일 필요는 없다.
    return HttpResponse('블로그 패턴 응답 완료')
#이 함수는 ^blog/$' 패턴에만 응답하도록 되어있다.
#사용자가 127.0.0.1:8000/blog 라고 들어가면 사용되는 함수이다. 만약 path를 blug 이런식으로 쓰면 안됨
#그냥 127.0.0.1:8000/ 라고만 치면 '^$' 패턴에 대한 것임

#만약 blog라는 path뿐만이 아닌 여러 path에 대해서도 어떤 함수를 동작시키고자 한다면 정규표현식으로 패턴을 나타내주면 된다.



#4. slug패턴 받은 것에 대하 선생님은 아래와 같이 함수를 구성하심
def viewOfPage(request, slug):
    res=' '.join(slug.split('-'))
    return HttpResponse('{}'.format(res))
#.split 및 .join 함수에 대한 것 -> https://wikidocs.net/13 참고



def viewOfYear(request):
    return HttpResponse('페이지 년도 페이지')

    
def viewOfMonth(request):
    return HttpResponse('페이지 월 페이지')

    
def viewOfDay(request):
    return HttpResponse('페이지 일 페이지')

    
def viewOfPage(request):
    return HttpResponse('페이지 그냥 보는 곳')




from django.shortcuts import render

def index(request):
    context ={
        'key1':'데이터1',
        'key2':100,
        'key3':[1,2,3,4],
        'key4':{'a':1,'b':2,'c':3},
    }
    return render(request, 'index.html', context)