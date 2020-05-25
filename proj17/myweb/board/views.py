from django.shortcuts import render, redirect
from board.models import Board, BoardComment
# Create your views here.

def boardIndex(request):
    if request.method == 'GET':
        data = Board.objects.all().order_by('-id')  #id가 아닌 작성일을 기준으로 가져올 수도 있음
        context = {
            'data':data   #search로 검색을 한 경우와 특정페이지를 요구한 경우, 그리고 기본페이지를 요구한 경우에 대해 다른 데이터 담기도록 해주면 될 듯
        }
        response = render(request, 'board/index.html', context)
    elif request.method == 'POST':
        response = redirect('/')
    return response


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
        context={
            'data':data
        }
        response = render(request, 'board/view.html', context)
    elif request.method == 'POST':
        response = redirect('/')
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
        response = redirect('/')
    return response

def boardCommentDelete(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        response = redirect('/')
    return response

#위 세개의 함수는 GET방식 쓰지 않을 것임. 처리에 있어서 다른 페이지를 먼저 보내주고 그 뒤에 처리하는 방식이 필요가 없기 때문
#즉 데이터베이스에 바로 적용을 시켜주면 되지, 사용자에게 그 데이터베이스에 값을 추가하기 위한 양식을 먼저 보낼 필요가 없다는 것임
#그러면 comment.html은 어디에 쓸 것인가? 저 html은 게시글을 보는 view.html의 하단에 include해서 댓글이 보이도록 처리할 것임