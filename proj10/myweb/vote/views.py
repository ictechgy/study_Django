from django.shortcuts import render, redirect


# Create your views here.
from vote.models import Question, Choices

def voteIndex(request):
    data = Question.objects.all()
    context = {
        'data':data
    }
    return render(request, 'vote/index.html', context) #app 디렉토리별로 템플릿 쓰려면 INSTALLED APPS에 앱 추가 필요!

def voteInsert(request):
    if request.method == 'GET':
        return render(request, 'vote/insert.html')
    elif request.method == 'POST':
        Question.objects.create(   #get이나 filter또는 이런 데이터베이스 건드리는 부분은 프로그래밍 문법과는 조금 다른건가. 동일한거 찾을 때 = 하나만 쓰는 것 등 
            title=request.POST.get('title'),
            author=request.POST.get('writer'),
            #start_date=request.POST.get('start_date', 'start_time'),
            #end_date=request.POST.get('end_date', 'end_time')   날짜와 시간에 대한 두 input값을 한 칼럼에 넣는 법
            start_date=request.POST.get('start_date')+" "+request.POST.get('start_time'),
            end_date=request.POST.get('end_date')+" "+request.POST.get('end_time')
        )
        #data = Question.objects.values_list('id', flat=True).all()
        data = Question.objects.values_list('id', flat=True).all().order_by('-id')
        Choices.objects.create(
            #q_id=data[-1], 아 네거티브인덱싱 못쓴다네
            q_id=data[0],
            text=request.POST.get('contents')
        )
        return redirect('/vote/') # 아 이건 또 왜 안돼

def voteUpdate(request):
    pass

def voteDelete(request):
    pass

def voteCheck(request, id):
    pass

def voteConfirm(request, id):
    pass



