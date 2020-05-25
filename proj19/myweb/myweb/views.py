from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
    context = {
        'key1': '데이터1',
        'key2': 102,
        'key3': [1, 2, 3, 4],
        'key4': {'a':1, 'b':2, 'c':3},
    }
    return render(request, 'index.html', context)

def join(request):
    if request.method == 'GET':
        context = {

        }
        response = render(request, 'registration/join.html', context)
    elif request.method == 'POST':
        # 회원 정보 저장
        if not User.objects.filter(username=request.POST.get('username')):
            data = User()
            data.username = request.POST.get('username')
            data.set_password(request.POST.get('password'))
            data.first_name = request.POST.get('first_name')
            data.last_name = request.POST.get('last_name')
            data.email = request.POST.get('email')
            data.save()
            
            response = redirect('login')
        else:
            response = redirect('join')

    return response


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