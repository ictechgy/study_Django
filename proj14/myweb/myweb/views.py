from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  #User테이블 사용하기


#index.html에서 사용자가 회원가입버튼을 눌렀다고 치자. 해당 버튼은 {% url 'join' %}인데 이는 /account/join/으로 연결시키는 버튼이며 해당 버튼을 통해
#url(r'^account/join/$', 'myweb.views.join', name='join') 패턴이 동작한다. 이에 따라 아래의 함수로 연결되게 된다.

#{% url 'join' %} 이 /account/join/이 되는건 페이지를 보내기 전 장고에서 알아서 해당 name또는 namespace 일치하는 것을 찾아서 url로 변경시켜서 보내는 것일 것

def join(request):
    if request.method=="GET":
        context = {

        }
        response = render(request, 'registration/join.html', context)
    elif request.method=="POST":  #회원가입 양식 값 다 받고 회원가입 다 시킨 후에 메인페이지로 연결시키기
        data = User()
        data.username = request.POST.get('username')
        # data.password = request.POST.get('password') #암호화가 되어 저장이 되어야 한다. 에러가 뜬다.
        data.set_password(request.POST.get('password'))
        data.first_name = request.POST.get('first_name')
        data.last_name = request.POST.get('last_name')
        data.email = request.POST.get('email')
        data.save()
        response = redirect('login')  #역순조회 사용.  /account/login/ 쓴 것과 동일
    return response

#username 중복 체크 필요
#테이블 칼럼속성보면 username은 30자 제한으로 되어있음. password는 어차피 암호화처리가 되므로 길이 상관 없음
#패스워드에 대해 두번 입력받게 만든다던지.. -> 자바스크립트와 같이 html 파일에서 구현하는게 아닌가?


    elif request.method=="POST":
        if not User.objects.filter(username=request.POST.get('username')): 
            #.count를 써서 반환 갯수를 봐도 됨. 반환되는게 0이라면 username이 존재하지 않는 상태라는거니까 해당 username으로 생성가능
            #get메소드써도 되지 않을까. 어차피 중복되는게 있다면 하나만 나올테니까.. 아 중복되는게 하나도 없는 경우 반환되는것은 없고 이 때 get은 오류를 내겠구나
            #[] 로 빈 리스트 나오면 이건 false를 의미하고 [<objects>]로 뭔가 중복되는게 나온다면 그건 True를 의미한다.
            data = User()                                   
            data.username = request.POST.get('username')
            data.set_password(request.POST.get('password'))
            data.first_name = request.POST.get('first_name')
            data.last_name = request.POST.get('last_name')
            data.email = request.POST.get('email')
            data.save()
            response = redirect('login')
        else:
            response = redirect('join')  #여기서 이렇게 다시 보내면 이전에 입력했던 값들은 다 사라지는거 아닌가
    return response









def index(request):
    context = {
        'key1': '데이터1',
        'key2': 102,
        'key3': [1, 2, 3, 4],
        'key4': {'a':1, 'b':2, 'c':3},
    }
    return render(request, 'index.html', context)

def blog(request):
    return HttpResponse('블로그 패턴 응답 완료')

def viewOfYear(request):
    return HttpResponse('년도 패턴 응답 완료')

def viewOfMonth(request):
    return HttpResponse('월 패턴 응답 완료')

def viewOfDay(request):
    return HttpResponse('일자 응답 완료')

def viewOfPage(request, slug):
    res = ' '.join(slug.split('-'))
    return HttpResponse('{}'.format(res))