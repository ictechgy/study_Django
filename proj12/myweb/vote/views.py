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

    #선생님이 만든 POST영역
    elif request.method == "POST":
        print(request.POST) #일단 값이 잘 넘어오는지 터미널창을 통해 확인하기 위함
        #넘어온 값을 보면 딕셔너리형태로 값이 넘어온다. 'end_time':['12:00'] 뭐 이런식으로.
        #choice에 대해서는 'choice'라는 키값에 대해 ['a', 'b', 'c', 'd']라는 밸류로 오게 된다.
        request.POST.get('title')
        request.POST.get('end_time')
        #get은 오직 하나만 가져온다. choice는 밸류가 리스트로 여러개가 있는데.. 0번인덱스값만 가져오는건가
        request.POST.getlist('choice')


#문제는 항목들을 text라는 칼럼에 한번에 보관했다고 치자
#그것들을 선택항목으로써 어떻게 분리해서 표시하며, 각각의 항목별로 선택된 횟수를 어떻게 나누는가?
#그리고 데이터베이스 테이블을 굳이 2개로 나눌 필요성이 있었는가

#받아온 데이터를 데이터베이스에 저장시켜보자
        data = Question()
        data.title = request.POST.get('title')
        data.author = request.POST.get('author')
        #시간저장양식은 "YYYY-MM-DD HH:MM::SS" 형식이여야 한다. 즉 "2018-06-26 12:00:00" 이런식이여야 한다.
        data.start_date = request.POST.get('start_date')+' '+request.POST.get('start_time')
        data.end_date = request.POST.get('end_date')+' '+request.POST.get('end_time')
        data.save()

        Choices.objects.create(q_id = data.id, text = request.POST.getlist('choice')[0])
        Choices.objects.create(q_id = data.id, text = request.POST.getlist('choice')[1])
        Choices.objects.create(q_id = data.id, text = request.POST.getlist('choice')[2])
        Choices.objects.create(q_id = data.id, text = request.POST.getlist('choice')[3])

    #카운트는 default를 0으로 지정해놓았으며 다른 사람이 선택을 한 경우에만 늘어나게 할 것이니 저장 할 필요가 없다.
        #또는
        for item in request.POST.getlist('choice'):
            Choices.objects.create(q_id=data.id, text=item)

        response=redirect('/vote/')

    return response
#아하 항목 갯수만큼 Choice테이블에 레코드를 추가하는구나.. q_id는 동일하게..
#그럼 각 항목별로 count를 따로 관리할 수 있겠구만 

#하나의 Question 에 대해 choice는 여러 레코드를 사용도록 구성

#아 그리고 현재 목록 보여지는게 최신글이 가장 아래에 보이게 되니.. 역순정렬해서 index.html에서 나오도록 해야한다.







def voteCheck(request, id):
    data1 = Question.objects.get(id=id)
    data2 = Choices.objects.get(q_id=id)
    context = {
        "data1":data1,
        "data2":data2
    }
    return render(request, 'vote/check.html', context)


#이제 글 목록에서 투표하려고 클릭시 해당 투표글로 넘어가는 것 만들기
def voteCheck(request, idx):
    if request.method == 'GET':
        data = Question.objects.get(id=idx)
        choices = choices.objects.filter(q_id=idx)
        context = {
            'data':data,
            'choices':choices
        }
        response = render(request, 'vote/check.html', context)



    #항목 카운트 올리기 2018-06-27
    elif request.method == "POST":
        idx #Question Table의 id이면서 Choices테이블의 q_id
        request.POST.get('choice') # Choices 테이블의 id값
        #사실 choices테이블의 id값만 가져와도 될 거 같긴 하다. 근데 굳이 form action에서 url 맨 뒤에 Question id값도 보낸 이유는 함수 자체가 두개의 인자를
        #받도록 설계되어있는데 아무것도 안보내면 오류떠서인거 아닌가?

        data = Choices.objects.get(id=request.POST.get('choice'), q_id=idx) # q_id에 대한 부분은 없어도 되긴 함
        data.count = data.count + 1
        data.save()

        response = redirect('/vote/confirm/{}/'.format(idx))  # 결과를 확인할 수 있는 페이지로 넘기기

    return response


#투표 완료 후 투표 결과값 페이지 띄우기
def voteConfirm(request, idx):
    if request.method == "GET":
        data = Question.objects.get(id=idx)
        choices = Choices.objects.filter(q_id=idx)
        context = {
            'data':data,
            'choices':choices
        }
        response = render(request, 'vote/confirm.html', context)

    elif request.method == "POST":
        pass
    
    return response





def voteUpdate(request):
    if request.method == "GET":
        data = Question.objects.get(id=request.GET.get('id'))
        choices = Choices.objects.filter(q_id=data.id)  #오호
        context = {
            'data':data,
            'choices':choices
        }
        response = render(request, 'vote/update.html', context)
    elif request.method == "POST":
        data = Question.objects.get(id=request.POST.get('id'))
        data.title=request.POST.get('title')
        data.author=request.POST.get('author')
        data.start_date=request.POST.get('start_date')+" "+request.POST.get('start_time')
        data.end_date=request.POST.get('end_date')+" "+request.POST.get('end_time')
        data.save()

        choices = Choices.objects.filter(q_id=data.id)
        for idx in range(len(choices)):
            choices[idx].text=request.POST.getlist('choice')[idx]
            choices[idx].save()

        response = redirect('/vote/check/{}/'.format(data.id))
    
    return response


def voteDelete(request):
    if request.method=="GET":
        data = Question.objects.get(id=request.GET.get('id'))
        context = {
            'data':data
        }
        response = render(request, 'vote/delete.html', context)

    elif request.method == "POST":
        Question.objects.get(id=request.POST.get('id')).delete()
        Choices.objects.filter(q_id=request.POST.get('id')).delete()  #get은 딱 1개만 받아옴. 없거나 2개이상이면 오류
        response=redirect('/vote/')

    return response

#틀은 이제 잡혔다. 추가적기능을 이제 만들면 된다.. 동적으로 항목 추가하는 기능?
#기간 안에서만 투표가 진행될 수 있게끔 한다던가. 기간이 지나면 투표 불가
#기간 지난 내용은 기본적으로 안보이게 만든다던가.. 기간이 지난 투표항목은 따로 볼 수 있게 한다던가 등등
