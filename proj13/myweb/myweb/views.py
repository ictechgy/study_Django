from django.http import HttpResponse
from django.shortcuts import render

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