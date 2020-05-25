from django.shortcuts import render, redirect
from vote.models import Question, Choices
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.
def voteIndex(request):
    if request.method == 'GET':
        data = Question.objects.all().order_by('-id')
        paging = Paginator(data, 5)
        if request.GET.get('page') == None: #page에 대한 요구정보가 없을경우. 즉 처음 페이지에 접근한 경우
            worth = paging.page(1)  #1페이지를 보여주겠다!
        else:
            pass

        context = {
            'data': worth
        }

        response = render(request, 'vote/index.html', context)

    return response

def voteInsert(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            context = {
                'date': datetime.now()
            }
            response = render(request, 'vote/insert.html', context)
        else:
            response = redirect('login')
            #로그인하지 않은 사용자가 투표추가 url에 접근하려 한다면 로그인페이지로 보내기. 
            #'login' -> /account/login/페이지를 재요구하게 됨. 로그인이 완료되면 settings.py에 의해 메인페이지로 연결됨. 로그인 이전의 페이지로 연결은 못하나
            #로그아웃시에는 /account/logout/ 페이지를 요구하게 되고 로그아웃처리가 자동처리 된 이후에 logged_out.html이 던져짐
    elif request.method == 'POST':
        data = Question()
        data.title = request.POST.get('title')
        data.author = request.POST.get('author')
        data.start_date = request.POST.get('start_date') + ' ' + request.POST.get('start_time')
        data.end_date = request.POST.get('end_date') + ' ' + request.POST.get('end_time')
        data.save()

        for item in request.POST.getlist('choice'):
            Choices.objects.create(q_id=data.id, text=item)

        response = redirect('vote:index')

    return response



def voteUpdate(request):
    if request.method == 'GET':
        data = Question.objects.get(id=request.GET.get('id'))
        if request.user.username == data.author:
            choices = Choices.objects.filter(q_id=data.id)
            context = {
                'data': data,
                'choices': choices
            }
            response = render(request, 'vote/update.html', context)
        else:
            response = redirect('vote:index')
    elif request.method == 'POST':
        data = Question.objects.get(id=request.POST.get('id'))
        data.title = request.POST.get('title')
        data.author = request.POST.get('author')
        data.start_date = request.POST.get('start_date') + ' ' + request.POST.get('start_time')
        data.end_date = request.POST.get('end_date') + ' ' + request.POST.get('end_time')
        data.save()

        choices = Choices.objects.filter(q_id=data.id)
        for idx in range(len(choices)):
            choices[idx].text = request.POST.getlist('choice')[idx]
            choices[idx].save()

        response = redirect('vote:check', data.id)
        #목록을 더 추가해서 수정한다던지 목록 삭제한다던지 하면 조금 더 복잡해질 수정페이지와 함수들
    return response
    

def voteDelete(request):
    if request.method == 'GET':
        data = Question.objects.get(id=request.GET.get('id'))
        if request.user.username == data.author:
            context = {
                'data': data
            }
            response = render(request, 'vote/delete.html', context)
        else:
            response = redirect('vote:index')
    elif request.method == 'POST':
        Question.objects.get(id=request.POST.get('id')).delete()
        Choices.objects.filter(q_id=request.POST.get('id')).delete()

        response = redirect('vote:index')

    return response

def voteCheck(request, idx):
    if request.method == 'GET':
        if request.user.is_authenticated():
            data = Question.objects.get(id=idx)
            choices = Choices.objects.filter(q_id=idx)
            context = {
                'data': data,
                'choices': choices
            }
            response = render(request, 'vote/check.html', context)
        else:
            response = redirect('login')
    elif request.method == 'POST':
        data = Choices.objects.get(id=request.POST.get('choice'), q_id=idx)
        data.count = data.count + 1
        data.save()

        response = redirect('vote:confirm', idx)

    return response

def voteConfirm(request, idx):
    if request.method == 'GET':
        data = Question.objects.get(id=idx)
        choices = Choices.objects.filter(q_id=idx)
        context = {
            'data': data,
            'choices': choices
        }
        response = render(request, 'vote/confirm.html', context)

    return response
