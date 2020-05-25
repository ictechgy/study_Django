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
#우리는 model을 만들어 데이터베이스에 어떤 테이블을 만들었고 어드민페이지에서 그 데이터베이스를 관리하는 방법을 배웠다.
#이제 view에서 model과 연결하여 사용자가 어떤 페이지를 요구 했을 때 model을 이용해 데이터베이스값을 받아오고 이를 html에출력하여 사용자에게 던져주는 것을 해보자

#모델과의 연결
from htm.models import htmTagTable  
#import해줘야 이 view에서 해당 model의 테이블을 쓸 수 있음. 즉 from을 이용해서 view와 model을 연결시키고 import를 통해 실질적 데이터베이스공간과도 연결하는 것같음
def mainIndex(request):  #사용자가 /htm/ 에 대한 메인페이지를 요구한다면 작동 될 함수
    data = htmTagTable.objects.all()   #테이블의 모든 것을 다 검색해서 가져오고 이를 data라는 변수에 할당시킨다.
    context = {
        'data' : data                     #딕셔너리에 담아서 html에 보낼 준비
    }
    return render(request, 'htm/index.html', context)
    #이렇게 하면 context딕셔너리의 data라는 밸류에(즉 data변수에) 가져온 것들이 리스트형식으로 들어가는 듯? 각각의 행에 대해서는 <> 으로 구분하고 한 행당
    #각각의 칼럼은 : 로 구분시켜서..


    #일부 컬럼만 가져오고 싶다면
    data = htmTagTable.object.values('id', 'tag_name').all()
    #저 오브젝트에서 칼럼 id와 tag_name에 해당하는 것만 전부 가져와라
    #이렇게만 해서 data를 딕셔너리에 넣어 보내면 html에서는 {{ data }}했을 시 object라고 뜨지는 않고 리스트형식으로 실질적 값이 다 보이긴 한다.
    #각각의 행은 {} 딕셔너리형태로 구분되어 보인다. [{1:hn}, {2:div}, {}] 이런 꼴로?
    # 이런 경우 실질적 값을 출력하고 싶다면 {{ data.1.1 }} 뭐 이런식으로 쓰면 됐을라나 

    #온점을 이용해서 특정 행에서 특정 칼럼에 대한 값만을 가져올 수 있다.
    #values()로 하면 각 행이 딕셔너리형태로 나오는데 values_list()로 가져오면 튜플형태로 html파일에서 쓸 수 있다.
    #따라서 이때에는 온점을 쓰는게 아니라 인덱스 번호를 써야한다.
    #아 그냥 object라고 하면 전부 가져오는거고, value를 쓰면 각 행별로 칼럼과 값을 딕셔너리형태로 매칭시켜서 가져오고
    #value_list라고 하면 column에 해당하는 키 부분은 사라지고 실질적 값들만 가져오게 되는 형태
    
    #정리
    data = htmTagTable.objects.all() #전부다 가져왔다면
    #이 때 data변수에 할당되는 형식은 아래와 같다.
    [<{'id':1, 'tag_name':'hn', 'tag_context':'내용'}>,<{}>,<{}>]   {{ data }} 로 한번에 출력 불가능한 형태

    data = htmTagTable.object.values('id', 'tag_name').all() #일부 칼럼만 가져왔다면
    [{'id': 1, 'tag_name': 'hn'}, {}, {}]

    data = htmTagTable.objects.values_list('id', 'tag_name').all() #values_list를 쓰면
    [(1, 'hn'), (), ()]  #키값에 해당하는 부분은 사라지게 됨

    #이렇게 받아진 내용들에 대해 반복문을 통해서 출력되도록 만들어도 되고 아니면 그냥 온점 참조연산자를 써도 된다.




    #이전에 htm 메인페이지인 index.html을 봤을 때 각각의 hn과 div unordered list목록을 이번에는 데이터베이스의 값을 이용해서 보여주고자 할 때

    data = htmTagTable.objects.values_list('tag_name').all()
    context = {
        'tag_list':data
    }
    
    
    <ul>
        {% for tag in tag_list %}
            <li><a href='/htm/tag/{{ tag.0 }}/'>{{ tag.0 }}</a></li>
        {% endfor %}
    </ul>
    #위의 방식은 인덱스번호가 쓰이는 방식. 인덱스번호를 쓰고 싶지 않다면 아래와 같이 작성

    data = htmTagTable.objects.values_list('tag_name', flat = True)   #두개 이상 칼럼에 대해 가져올 경우 flat쓰지 말 것 -> 오류가 뜨는건지 아니면 행에 대한 구분이 사라지니 그런건가
    flat = True 속성을 쓰면 튜플이 벗겨진다
    <ul>
        {% for tag in tag_list %}
            <li><a href='/htm/tag/{{ tag }}/'>{{ tag }}</a></li>
        {% endfor %}
    </ul>


#각각의 목록을 클릭했을 때 이제 해당하는 html을 일일히 선택적으로 보내주는게 아니라 데이터베이스에 있는 tag_context값을 보여주고 싶다면
    def htmTag(request, tag):
        data = htmTagTable.objects.values('tag_name', 'tag_context').get(tag_name=tag)  #all대신에 get 오로지 하나 행만을 가져올때 쓰는 함수
        context = {
            'data':data
        }
        return render(request, 'htm/tags.html', context)  #tags.html파일 보기
        #코드가 너무 길면 중간중간에 \로 끊고 다음줄에 작성 가능

        #get을 통해 검색조건을 설정 할 수 있다. 검색조건은 여러개 설정가능하다.
        #검색조건에서의 문법이 독특하다. 칼럼명을 따옴표로 감싸주지도 않으며 같다는 기호 == 를 쓰는게 아니라 등호 하나만을 쓴다.

#get을 이용하여 가져와진 데이터는 리스트형식이 아니다. 여러개였다면 리스트에 묶였겠지만 한줄만 가져오므로 리스트가 바깥쪽에 감싸져있지 않음
{'tag_name': 'hn', 'tag_context': 'hn태그에 대한 예시'}
#하나의 딕셔너리에 담긴 형태로 받아와짐. 일단 values를 썼으니 키와 밸류가 묶인 형태로 되어있고..

#values_list로 받아오는 경우
('hn', 'hn태그에 대한 예시')
#이와 같이 받아와진다. 

#만약에 
data = htmTagTable.objects.all().get(tag_name=tag) #이렇게 받아오고 {{ data }}출력해본다면?
일단은 htmTagTable object 라고만 뜬다. 이 때 {{ data.tag_name }} 또는 {{ data.tag_context }} 하니까 내부 값이 나오긴 함
약간 이런 식으로 받아진건가. data = <{'id':1, 'tag_name':'hn', 'tag_context':'내용'}>
# 그럼 여기서 <> 가 의미하는건 뭘까. 암호화같은 느낌인데. 그냥은 다 안보이게 막아두는?


#그리고 위에서는 
data = htmTagTable.objects.values('tag_name', 'tag_context').get(tag_name=tag)
#이렇게 했는데, 
data = htmTagTable.objects.values('tag_context').get(tag_name=tag) #이렇게 해도 되지 않나?
#ㅇㅇ 그렇게 해도 된다. 이렇게 한 경우 data에 할당되는 값은 
{'tag_context': 'hn태그에 대한 예시'}
#이런 방식이네. 그러면 그냥 value_list써도 되긴 할 듯 바로 {{ data }} 로 내용 출력 가능하게


#search창에 대해서도 검색 했을 때 각각의 html파일을 연결시키는게 아니라 데이터베이스의 값을 보여주고자 한다면.
def htmSearch(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        data = htmTagTable.objects.values('tag_name', 'tag_context').get(tag_name=search)
        context = {
            'data':data
        }
        return render(request, 'htm/tags.html', context)
# html파일에서는 이제 {{ data.tag_context }} 로 출력하면 완료

#그리고 이제 ul로 hn이나 div등 index.html파일에서 목록 보여주던 것도 데이터베이스에 있는 값을 기준으로 만든다면
def mainIndex(request):
    data = htmTagTable.objects.values_list('tag_name', flat=True).all()
    context = {
        'tag_list' : data
    }
    return render(request, 'htm/index.html', context) 
#이렇게 하고 index.html에서는 
    <ul>
        {% for tag in tag_list %}
            <li><a href='/htm/tag/{{ tag }}/'>{{ tag }}</a></li>
        {% endfor %}
    </ul>
#이걸로 출력하면 됨

#다만 flat속성을 주지 않으면
data = [('hn'),('div'),('a')] 뭐 이런식으로 받아와짐
#그러면 index.html에서 출력되는것도 괄호가 포함된 형식으로 보이고, 링크를 타고 요구할 수 있는 URL도 이상해져서 링크 클릭 시 페이지 못찾게 됨


#2차 정리
.all() 로 모든 값을 가져올 때 값이 여러개라면 리스트에 묶인채로 가져오게 된다.
만약 가져온 값이 하나라고 하더라도 그건 리스트로 묶여있을까

.get()으로 한 행의 값을 가져올 때에는 리스트로 묶인 형태로 오지 않는다.

objects.all() 로 모든 것을 가져오게 되면 
[<{'칼럼명':값, '칼럼명':값}>, <{'칼럼명':값, '칼럼명':값}>, <{}>, <{}>] 이런 형태로 값을 가져오게 된다. 각각의 행은 <>로 구분.
그리고 한번에 다 출력하여 볼 수가 없다. 단순히 Object라고만 뜬다. 즉 [<테이블명 : 테이블 Object>,<테이블명 : 테이블 Object>] 단순형태
보고싶다면 인덱스번호에다가 키값까지 추가하든지 아니면 for문으로 하나하나 할당시키면서 키값으로 출력시키든지

values()와 values_list 의 차이
values()는 값을 가져올 때 칼럼명과 값을 1:1 매칭시켜서 가져온다.
예를 들면 {'칼럼명':값, '칼럼명':값, '칼럼명':값} 이런식으로 말이다. 한 줄의 하나의 칼럼만을 가져온다고 해도 {'칼럼명':값}으로 묶인다.
만약 여러줄에 대해 가져온다면 
[{'칼럼명':값, '칼럼명':값}, {'칼럼명':값, '칼럼명':값}, {'칼럼명':값, '칼럼명':값}] 이런 형식으로 가져오게 된다. 

values_list는 이런 딕셔너리형태를 없앤 함수다. 즉, 키값은 없애고 실질적 값만 가져온다. 튜플형태로
한 행의 한 칼럼만을 대상으로 한다면 ('값')
한 행의 여러 칼럼을 대상으로 한다면 ('값', '값', '값')
여러 행의 한 칼럼만을 대상으로 한다면 [('값'), ('값'), ('값')] 
여러행의 여러 칼럼을 대상으로 한다면 [('값', '값', '값'), ('값', '값', '값'), ('값', '값', '값')]
flat으로 소괄호를 제거할 수 있다. 즉 행에 대한 구분인 ()를 제거하는 flat=True 속성


search = Research.objects.get(id=10) 이렇게만 쓰면
{{ search }} 했을 시 <Research: Research object> 이렇게만 뜨는 듯.
내부 구조는 역시나 <{'칼럼값':값, '칼럼값':값, '칼럼값':값}> 이런 형태일 듯 

.all() 이 먼저쓰이든 .values()가 먼저쓰이든 순서는 상관이 없는듯
아 그러면 결국 데이터베이스명.object 에서 이미 모든 값에 대한 접근은 끝나는 듯
모든 값중 내가 원하는 칼럼부분만 가져오든, 내가 원하는 칼럼에 대해 모든 값을 가져오든 순서는 중요치 않은 듯 하다.