from django.shortcuts import render, redirect
from vote.models import Question, Choices

# Create your views here.
def voteIndex(request):
    if request.method == 'GET':
        data = Question.objects.all().order_by('-id')
        context = {
            'data': data
        }
        response = render(request, 'vote/index.html', context)
    elif request.method == 'POST':
        pass

    return response




def voteInsert(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            response = render(request, 'vote/insert.html')
        else:
            response = redirect('vote:index')
            response = redirect('login')
#로그인한 유저만 /vote/insert/ url에 접근가능하도록 만듬
#로그인 안한 유저가 해당 url로 접근시 vote 메인페이지로 연결시키거나 로그인페이지로 연결시키거나
#이거 보니까 인터넷 배달음식 주문에서 url 주소 숫자값 조금만 건드리면 다른사람 정보 볼 수 있던거 생각나네
#get방식 요청으로 배달데이터 처리해서인거 아닌가
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
        choices = Choices.objects.filter(q_id=data.id)
        context = {
            'data': data,
            'choices': choices
        }
        response = render(request, 'vote/update.html', context)
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

    return response

def voteDelete(request):
    if request.method == 'GET':
        data = Question.objects.get(id=request.GET.get('id'))
        context = {
            'data': data
        }
        response = render(request, 'vote/delete.html', context)
    elif request.method == 'POST':
        Question.objects.get(id=request.POST.get('id')).delete()
        Choices.objects.filter(q_id=request.POST.get('id')).delete()

        response = redirect('vote:index')

    return response

def voteCheck(request, idx):
    if request.method == 'GET':
        data = Question.objects.get(id=idx)
        choices = Choices.objects.filter(q_id=idx)
        context = {
            'data': data,
            'choices': choices
        }
        response = render(request, 'vote/check.html', context)
    elif request.method == 'POST':
        # idx # Question Table의 id, Choices Table의 q_id
        # request.POST.get('choice')  # Choices Table의 id
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
    elif request.method == 'POST':
        pass

    return response
