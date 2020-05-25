from django.shortcuts import render, redirect
from board.models import Board, BoardComment
# Create your views here.

from django.core.paginator import Paginator

def boardIndex(request):
    if request.method == 'GET':
        data = Paginator(Board.objects.all().order_by('-id'), 1)  #id가 아닌 작성일을 기준으로 가져올 수도 있음
        page = data.page(request.GET.get('page'),1)
        st_num = 0 if page.number - 3 < 0 else page.number - 3   #'if식'이라고 한다.
        ed_num = st_num + 5
        context = {
            'data':page, #data.page(request.GET.get('page', 1)),
            'page_range':data.page_range[st_num:ed_num]         #슬라이싱
        }
        response = render(request, 'board/index.html', context)
    elif request.method == 'POST':
        response = redirect('/')
    return response
#만약 사용자가 1~3페이지에 대한 부분을 보고 있었다고 하자. 그러면 page변수에는 해당 페이지에 대한 값만이 담기게 된다.
#이 때 if식에 의해 st_num에는 0이라는 값이 담기고 ed_num에는 5라는 값이 담긴다. 슬라이싱부분에 의하여 data.page_range[0:5]가 되는데 이는 0~4번 인덱스의 값을 잘라내는 
#것이고 1페이지~5페이지의 page_range를 가지고 가게된다. 즉 사용자가 보는 페이지에는 1~5페이지 버튼만 보이게 된다.

#사용자가 4페이지버튼을 눌렀다고 하자. 그러면 st_num은 1이 된다. ed_num은 6이 되고 [1:6]슬라이싱에 의해 1~5번 인덱스의 페이지레인지 리스트값을 잘라내게 된다.
#이는 2페이지~6페이지를 의미하게 되고 사용자가 그 결과인 4페이지 데이터베이스 값을 보게 되었을 때 페이지 이동 링크에는 2~6페이지 버튼이 보이게 된다.

#만약에 페이지가 10페이지까지 있다고 치자. 사용자가 9페이지나 10페이지를 요구한 경우에는? 9페이지를 요구했다고 하자.
#st_num은 6이 되고 ed_num은 11이 된다. data.page_range[6:11]에 의해 6번인덱스~10번 인덱스의 값을 잘라내게 되는데, 애초에 페이지레인지에는 9번인덱스까지만 존재한다.
#그러면 그냥 끝 인덱쓰까지만 잘라내게 되는듯. 즉 6번인덱스~9번인덱스값만 잘라내게 되고 7페이지~10페이지버튼만 보이게 되는 듯

#마찬가지로 10페이지를 보려고 하게 된다면 [7:12] 슬라이싱을 하게되지만 7번인덱스~9번인덱스의 값만을 보게 되고 이는 8페이지~10페이지값을 볼 수 있게 된다. 

#이런식으로 해서 일정 갯수의 페이지 링크만 보이도록 선생님은 구현하셨다...

#만약 page.number -3 에서 숫자가 -4이거나 -2라면..
#-4였다면 사용자는 1~4페이지까지는 1~5페이지값을 볼 수 있게 되고 5페이지를 보려고 하면 2페이지~6페이지를 볼 수 있게 된다. 
#10페이지까지 있다고 가정했을 때 10페이지를 보려는 상황이라면 7페이지~10페이지를 볼 수 있게 된다.

#-2였다면? 1~2페이지까지는 1~5페이지를 볼 수 있으며 3페이지를 보게 되는 경우 2페이지~6페이지를 볼 수 있게 된다. 

#뭐 이와 반대로 아래 ed_num의 숫자값을 조정함으로서 볼 수 있는 페이지 레인지의 범위를 또 조정할 수도 있을 것임. 숫자가 커질수록 한번에 볼 수 있는 페이지 번호도
#많아질 것



from board.forms import BoardForm
def boardInsert(request):
    if request.method == 'GET':
        forms=BoardForm(initial={'author':request.user.username}) #초기값 설정
        context={
            'forms':forms
        }
        response = render(request, 'board/insert.html', context)
    elif request.method == 'POST':
        Board.objects.create(  #데이터베이스에 추가하는 것도 몇가지 방법이 더 있긴 함
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            content=request.POST.get('content')
        )
        response = redirect('board:index')
    return response


def boardView(request, idx):
    if request.method == 'GET':
        data = Board.objects.get(id=idx)
        comment = BoardComment.objects.filter(board_id=idx).order_by('-id')
        context={
            'data':data,
            'comment':comment
        }
        response = render(request, 'board/view.html', context)
    elif request.method == 'POST':
        response = redirect('board:view', idx)
    return response


def boardUpdate(request):
    if request.method == 'GET':
        response = render(request, 'board/update.html')
    elif request.method == 'POST':
        response = redirect('/')
    return response

def boardDelete(request):
    if request.method == 'GET':
        response = render(request, 'board/delete.html')
    elif request.method == 'POST':
        response = redirect('/')
    return response




def boardGoodBad(request, idx):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        response = redirect('/')
    return response

def boardCommentAdd(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        BoardComment.objects.create(
            board_id=request.POST.get('id'),  #model과 칼럼명이 같은지. 그리고 가져오려는 name속성값이 같은지
            author=request.POST.get('author'),
            content=request.POST.get('content')
        )
        response = redirect('board:view', request.POST.get('id'))
    return response

def boardCommentDelete(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        BoardComment.objects.get(id=request.POST.get('id')).delete()
        response = redirect('board:view', request.POST.get('board_id'))
    return response

#위 세개의 함수는 GET방식 쓰지 않을 것임. 처리에 있어서 다른 페이지를 먼저 보내주고 그 뒤에 처리하는 방식이 필요가 없기 때문
#그러면 comment.html은 어디에 쓸 것인가? 저 html은 게시글을 보는 view.html의 하단에 include해서 댓글이 보이도록 처리할 것임