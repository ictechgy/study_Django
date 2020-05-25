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

#파이썬에서 input함수로 사용자의 값을 받는 것은 기본적으로 문자로 받아지는데 이런 html로 받아지는 것도 동일하게 문자로 받아진다. 따라서 int()함수 사용이 필요하다
#자바로는 Integer.parseInt()
#근데 만약 사용자가 잘못된 값을 입력하면 오류 뜰 듯. 그 때에는 이 함수안에서 유효성 검사를 할 수도 있고 아니면 form쪽에서 먼저 자바스크립트로
#검증하여 올바른 값만 전송시키도록 만들 수도 있을 것이다.


#한 페이지에 결과도 보여주고 싶다면(calc.html에서 값을 입력받고 결과도 동일 페이지 내에서 뜨도록 만들기)
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

#아 내가 조건식에서 and가 아니라 &&를 썼구나. ㅋㅋㅋ &써도 오류 뜸. 그래서 and로 바꾸니 오류가 안뜬다.