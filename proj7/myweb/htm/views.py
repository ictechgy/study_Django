from django.shortcuts import render

# Create your views here.




def mainIndex(request):
    return render(request, 'htm/index.html')

def htmTag(request):
    return render(request, 'htm/tag.html')

def htmAdd(request, orn):
    add={
        "path":orn,
    }
    return render(request, 'htm/additional.html',add)
    #render로 다음에 넘겨줄 때에는 무조건 사전형으로 넘겨줘야한다고 하심. 오류뜨길래 보니까.




#2018-06-18
def htmSearch(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        return render(request, 'htm/{}.html'.format(search))  
#사용자가 입력하여 검색버튼을 누른 것에 대한 html파일 이름을 똑같이 찾아 전송

#실습
def htmCalc(request):
    return render(request, 'htm/calc.html')
def htmResult(request):
    if request.method == 'GET':
        num1=request.GET.get('num1')
        num2=request.GET.get('num2')
#함수에서 계산을 하고 html파일로 보낼 수도 있고 아니면 두 값을 다 보내서 html파일에서 계산을 할 수도 있음
        #res=num1+num2 #사용자가 입력한 숫자가 '숫자'값으로 올지 '문자'값으로 올지 아직 모르겠음
        #이런. 문자값으로 들어오는 군
        #res=(int)num1+(int)num2 이거 안되네 parse어케 해야하지
        res=int(num1)+int(num2)  #이렇게 하는군.. 아스키코드 관련해서는 chr()과 ord() 있음
        context={
            'res':res
        }
        return render(request, 'htm/calc_result.html', context)

#input함수도 문자로 받아지는데 이런 html로 받아지는 것도 동일하게 문자로 받아진다. 따라서 int()함수 사용이 필요하다
#자바로는 Integer.parseInt()
#근데 만약 사용자가 잘못된 값을 입력하면 오류 뜰 듯. 그 때에는 이 함수안에서 검사를 할 수도 있고 아니면 form쪽에서 자바스크립트로
#검증하여 올바른 값만 전송시키도록 만들 수도 있을 것이다.


#한 페이지에 결과도 보내고 싶다면
def htmCalc(request):
    if request.method == 'GET':
        if request.GET.get('num1') != None and request.GET.get('num2') != None:  #근데 왜 여기서 구문오류뜨냐 이건 모르겠군
            num1=request.GET.get('num1')
            num2=request.GET.get('num2')
            res=int(num1) + int(num2)
            context = {
                'res':res
            }
            return render(request, 'htm/calc.html', context)
        else:
            return render(request, 'htm/calc.html')

#초기에 페이지를 요청하면 아예 num1과 num2라는 인자 parameter 변수는 존재하지 않는다.
#그래서 그 상태에서 request.GET.get('num1') 를 하면 오류가 뜨는건가? 흠. None 또는 '' 인게 아닌건가 
# -> None이라는데 왜 위의 문법오류 발생?
#이 때 값이 존재하지 않는다면 기본값을 쓰도록 만들 수 있다. 선생님 파일 참고

#아 내가 저 and가 아니라 &&를 썼구나. ㅋㅋㅋ &써도 오류 뜸. 그래서 and로 바꾸니 오류가 안뜬다.




#2018-06-19
#모델과의 연결
from htm.models import htmTagTable 
def mainIndex(request):
    data = htmTagTable.object.all()   #테이블의 모든 것을 다 검색해서 가져오기. 
    context = {
        'data' : data                     #딕셔너리에 담아서 html에 보낼 준비
    }
    return render(request, 'htm/index.html', context)
    #이렇게 하면 data라는 밸류에 가져온 것들이 리스트형식으로 들어가는 듯? 각각의 행에 대해서는 <> 으로 구분하고 한 행당
    #각각의 칼럼은 : 로 구분시켜서..


    #일부 컬럼만 가져오고 싶다면
    htm.TagTable.object.values('id', 'tag_name').all()
    #저 오브젝트에서 id와 tag_name에 해당하는 것만 전부 가져와라
    #이렇게만 해서 data로 넣어 보내면 html에서는 {{ data }}했을 시 리스트형식으로 object라고 뜨지는 않고 실질적 값이 다 보이긴 한다.
    #각각의 행은 {} 딕셔너리형태로 구분되어 보인다. [{}, {}, {}] 

    #이전과 똑같이 온점을 이용해서 특정 칼럼에 대한 값만을 가져올 수 있다.
    #values()로 하면 딕셔너리형태로 나오는데 values_list()로 가져오면 튜플형태로 html파일에서 쓸 수 있다.
    #따라서 이때에는 온점을 쓰는게 아니라 인덱스 번호를 써야한다.
    #아 그냥 object라고 하면 전부 가져오는거고, value를 쓰면 각 행별로 칼럼과 값을 딕셔너리형태로 메칭시켜서 가져오고
    #value_list라고 하면 column에 해당하는 키 부분은 사라지고 실질적 값들만 가져오게 되는 형태
    

    #이전에 각각의 hn과 div목록을 이번에는 데이터베이스의 값을 이용해서 보여주고자 할 때

    data = htm.TagTable.object.value_list('tag_name').all()
    context = {
        'tag_list':data
    }
    
    
    <ul>
        {% for tag in tag_list %}
            <li><a href='/htm/tag/{{ tag.0 }}/'>{{ tag.0 }}</a></li>
        {% endfor %}
    </ul>


    htm.TagTable.object.value_list('tag_name', flat = True)   #두개 이상 칼럼에 대해 가져올 경우 flat쓰지 말 것
    flat = True 속성을 쓰면 튜플이 벗겨진다
    <ul>
        {% for tag in tag_list %}
            <li><a href='/htm/tag/{{ tag }}/'>{{ tag }}</a></li>
        {% endfor %}
    </ul>


#각각의 목록을 클릭했을 때 이제 해당하는 html을 일일히 선택적으로 보내주는게 아니라 데이터베이스에 있는 context값을 보여주고 싶다면
    def htmTag(request, tag):
        data = htmTagTable.object.values('tag_name', 'tag_context').get(tag_name=tag)  #all대신에 get 오로지 하나만을 가져온다
        context = {
            'data':data
        }
        return render(request, 'htm/tags.html', context)  #tags.html파일 보기
        #코드가 너무 길면 중간중간에 \로 끊고 다음줄에 작성 가능

        #get을 통해 검색조건을 설정 할 수 있다. 검색조건은 여러개 설정가능하다.


#search창에 대해서도 각각의 html파일을 연결시키는게 아니라 데이터베이스의 값을 보여주고자 한다면.





#2018-06-20
from htm.models import htmTagTable 
from django.shortcuts import render, redirect  #redirect쓰려면 render가져온 곳에서 redirect도 가져와야 한다.

def htmAdd(request):
    if request.method == 'GET':
        return render(request, 'htm/add.html')
    elif request.method == 'POST':  #데이터베이스에 데이터를 저장하기 위한 코드 작성
        name = request.POST.get('tag_name')
        context = request.POST.get('tag_context')
        htmTagTable.objects.create(tag_name=name, tag_context=context)
        #왼쪽에 있는 것은 칼럼이름 = 오른쪽에 있는 것은 칼럼에 저장하고자 하는 값이 있는 변수 이름
        return redirect('/htm/')
        #데이터베이스에 값이 추가가 됐는지 안됐는지에 따라 사실 다른 결과를 알려줘야 할 것 같은데
        #예기치 못한 오류에 대한 페이지..

        #그리고 두번째 조건식을 그냥 if로 해도 될테고.. else로 해도 될테고.. 큰 차이는 없음
        #if로 둔다고 해도 중복검증이 되는게 아니라 위에서 return이 있으니 중복검증될 상황은 안일어난다.

        #여기까지 다 만들면 사용자가 저장을 눌렀을 시 페이지가 메인페이지로 돌아가며, 만든 것이 보이게 된다.
        #해당 링크를 클릭하면 이에 해당하는 데이터베이스를 연결시켜주었기 때문에 결과값이 잘 나온다. autoescape off