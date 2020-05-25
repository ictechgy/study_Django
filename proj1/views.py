#만든 views.py 파일

#함수명은 index로 만들기로 했었다.
#def index():
#    pass     --> 일단 함수의 내용을 지금 적지 않겠다는 명령어임
#여기까지 하면 함수 못찾았다는 것은 안뜨지만 오류가 난다.

#함수에 인자 하나는 있어야 한다. request인자 꼭 필요

#def index(request):
#    pass
# Client에서는 HTTP Request를 하는데 인자를 서버에서는 모두 받아서 view로 보낸다. 페이지를 구성하고 만들고자 할 때에는 사용자 Client가 명시적으로
#어떤 값을 보내지 않는다고 하더라도 request를 통해 보내는 값은 존재할 것이며 서버에서는 이를 꼭 받아줘야 할 것이다.

#근데 또 오류가 난다. 받기는 했지만 return이 없어서 오류. 서버가 request를 받고 결과를 처리한 뒤 response 응답을 안해줘서그럼


from django.http import HttpResponse
# Http 규격에 맞춘 response전송 함수를 쓰기 위한 import.

def index(request):
    return HttpResponse('응답완료') #실질적으로 보내고자 하는 데이터를 서버에서 클라이언트로 보낸다.
    #여기까지 하면 일단 Model이나 Template부분은 쓰지 않고 바로 '응답완료'메시지를 클라이언트로 보낸 것. 웹에 저 글자가 뜬다.