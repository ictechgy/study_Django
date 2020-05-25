from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.

def viewOfYear(request):
    return render(request,'blog/index.html')

    
def viewOfMonth(request):
    return HttpResponse('블로그 페이지 월 페이지')

    
def viewOfDay(request):
    return HttpResponse('블로그 페이지 일 페이지')

    
def viewOfPage(request):
    return HttpResponse('블로그 페이지 그냥 보는 곳')

#다중으로 커서 만들고 쓰려면 Alt키 누르고 마우스로 여러곳 클릭한 다음에 쓰면 된다.