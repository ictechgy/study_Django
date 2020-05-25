from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def viewOfYear(request):
    return render(request, 'blog/index.html')

def viewOfMonth(request):
    return HttpResponse('blog viewOfMonth 응답 완료')

def viewOfDay(request):
    return HttpResponse('blog viewOfDay 응답 완료')

def viewOfPage(request):
    return HttpResponse('blog viewOfPage 응답 완료')
