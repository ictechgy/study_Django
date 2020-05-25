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
        print(request.POST.get('title'))
        print(request.POST.get('end_time'))
        #get은 오직 하나만 가져온다. 즉 키값에 해당하는 밸류가 리스트로 존재하기는 하는데 그 리스트들 중에서 단 하나만을 가져온다.
        #choice는 밸류가 리스트로 여러개가 있는데.. 0번인덱스값만 가져오는건가
        print(request.POST.get('choice'))
        print(request.POST.getlist('choice')) #리스트 그대로 온전히 가져오려면 getlist를 써야 한다.


#문제는 선택 항목들을 text라는 칼럼에 한번에 보관했다고 치자
#그것들을 선택항목으로써 어떻게 분리해서 표시하며, 각각의 항목별로 선택된 횟수를 어떻게 나누는가?
#그리고 데이터베이스 테이블을 굳이 2개로 나눌 필요성이 있었는가

#이에대한 궁금증은 아래에서 해결된다.


#받아온 데이터를 데이터베이스에 저장시켜보자
        data = Question()
        data.title = request.POST.get('title')
        data.author = request.POST.get('author')
        #시간저장양식은 "YYYY-MM-DD HH:MM:SS" 형식이여야 한다. 즉 "2018-06-26 12:00:00" 이런식이여야 한다.
        #그러한 형태여야지만 데이터베이스 중에서 DataTimeField에 값을 저장할 수 있다.
        data.start_date = request.POST.get('start_date')+' '+request.POST.get('start_time')
        data.end_date = request.POST.get('end_date')+' '+request.POST.get('end_time')
        data.save()

        #여기까지 해서 사용자가 만든 투표 하나에 대해서 Question 데이터베이스테이블에 한 레코드로서 추가하였다.
        #사용자의 투표 내용중에서 각각의 항목에 대해서는 Choices라는 테이블에 저장을 할 것인데, 선택항목이 여러개라면 그 갯수와 동일하게 각각의
        #레코드들을 생성하고 항목을 저장시킬 것이다. 이 때 q_id라는 칼럼을 둠으로서 하나의 Question 투표에 대해서 여러개의 Choices 레코드들을 한번에 관리할 수 있도록
        #한다. 

        Choices.objects.create(q_id = data.id, text = request.POST.getlist('choice')[0])
        Choices.objects.create(q_id = data.id, text = request.POST.getlist('choice')[1])
        Choices.objects.create(q_id = data.id, text = request.POST.getlist('choice')[2])
        Choices.objects.create(q_id = data.id, text = request.POST.getlist('choice')[3])
        #q_id를 설정 할 때 위에서 만든 data 변수를 바로 사용 가능하다. 현재 data라는 변수에는 갓 생성한 레코드 한 줄에 대한 정보가 다 담겨있다.
        #data = Question()을 했을 때 data변수에는 id에 해당하는 부분에 숫자값만 있고 다른 칼럼에는 아무런 값도 없었겠지만 값을 넣어줬고 save도 해줬었음 

        #Choices테이블의 각 레코드에서, 카운트는 default를 0으로 지정해놓았으며 다른 사람이 선택을 한 경우에만 늘어나게 할 것이니 어떤 값을 저장 할 필요가 없다.

        
        #위에서 Choices 테이블에 대한 레코드 추가는 아래의 반복문으로 대체 가능하다.
        for item in request.POST.getlist('choice'):
            Choices.objects.create(q_id=data.id, text=item)

        response=redirect('/vote/')

    return response

#아하 선택항목 갯수만큼 Choice테이블에 레코드를 추가하는구나.. q_id는 동일하게..
#그럼 각 항목별로 count를 따로 관리할 수 있겠구만 

#하나의 Question 에 대해 choice는 여러 레코드를 사용도록 구성  -> 이걸 몰라서 애먹고 있었음...
#그러면 데이터베이스 테이블을 하나로 만들어서는 관리하기가 어려운건가..
#TextField()에 모든 선택항목들을 다 집어넣되 특정 기호나 엔터를 기준으로 넣고, 이에 대해서 불러올 때 기준자를 기준으로 불러오도록 만든다던가..
#근데 이렇게 하면 선택횟수를 관리하기가 어려운가

#이렇게 하나의 앱이나 프로젝트에 대해 하나의 데이터베이스 테이블을 고집할 것이 아니라 여러개를 쓰도록 할 수도 있구나..


#아 그리고 현재 index.html 에서 목록 보여지는게 최신글이 가장 아래에 보이게 되니.. 역순정렬해서 index.html에서 나오도록 해야한다.










def voteUpdate(request):
    pass

def voteDelete(request):
    pass

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
    elif request.method == 'POST':
        #url을 통해 idx라는 변수로 넘어오는 것은 Question 테이블에서의 id값이고
        #사용자의 선택으로 choice라는 radio타입에 담겨오는 것은 Choices테이블에서의 레코드 하나의 id값이다. 
        #어떠한 것이 선택되었는지 choices의 id값을 통해 찾아가 count를 1 올려주고.. 선택을 완료했던 사용자 클라이언트에게는 어떤 페이지를 돌려주면 좋을까?
        #그리고 굳이 선택을 완료하고 전송을 할 때 어떤 Question이었는지 Question에서의 id값은 없어도 되지 않나?
        #아 근데 값을 뭐라도 넘겨주지 않으면 이 함수에서 받는 값은 두개인데 request하나만 넘겨주는 방식이 되서 오류가 뜰 수도 있는건가.


    return response


def voteConfirm(request, id):
    pass



