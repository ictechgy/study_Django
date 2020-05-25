from django.shortcuts import render, redirect, HttpResponse
from board.models import Board, BoardComment
# Create your views here.

from django.core.paginator import Paginator

def boardIndex(request):
    if request.method == 'GET':
        if request.GET.get('search') != 'None' and request.GET.get('search'):
            data = Board.objects.filter(title__contains=request.GET.get('search')).order_by('-create_date')
            #기본적으로는 title을 가지고 검색을 하게 했는데 작성자나 게시글 내용에 대해서 검색을 만들 수도 있을 것이다.
        else:
            data = Board.objects.all().order_by('-create_date') #검색어를 입력한 상태가 아니라면
        data = Paginator(data, 5)                           #id 또는 작성일을 기준으로 정렬하여 가져올 수 있다
        page = data.page(request.GET.get('page', 1))
        st_num = 0 if page.number - 3 < 0 else page.number - 3   #if식이라고 한다.
        ed_num = st_num + 5
        context = {
            'data':page, #(request.GET.get('page', 1)),
            'page_range':data.page_range[st_num:ed_num],
            'search':request.GET.get('search')
        }
        response = render(request, 'board/index.html', context)
    elif request.method == 'POST':
        response = redirect('/')
    return response
    #근데 이렇게 만들었을 때 검색한 것에 대해 데이터가 엄청 나왔다고 치자. 그럼 그 경우에도 페이지가 여러개 생성이 된다.
    #그 경우에 있어서 다음 페이지 버튼을 눌렀을 때에도 제대로 작동이 될 수 있을까?
    #역시나 제대로 작동 안된다. 그 부분은 건드려줘야 할 것같다.
    #예를 들어 검색한 것에 대해 한 페이지가 넘어가는 데이터가 생성이 되었고 index.html에서 페이지를 나눠서 보여준다고 치자
    #다음 페이지를 보기 위해 다른 페이지 번호를 누르는 순간 기존의 search에 담겨있던 값은 버려지고 서버로는 페이지정보만 넘어가게 된다.
    #따라서 기존의 모든 데이터에 대한 값 중 해당 페이지에 대한 데이터를 보게 된다. 

    #따라서 그러한 상태를 막아주기 위해 혹시나 search한 것이 있다면 해당 search정보도 지속적으로 넘겨주기 위해 index.html의 페이지 버튼에서 search
    #정보도 또 넘겨줄 수 있도록 만들어주었다. 이렇게 하니 검색한 것에 대해서 페이지가 여러개인 경우 다음 페이지들을 정상적으로 볼 수 있다.
    #즉 기존에는 그냥 페이지정보만 넘기게 되서 제대로 작동 안하다가, 나 이 페이지원하는데 다만 ~~걸 검색하고 있었어! 라고 알려주는 식이 된다.

    #근데 그냥 기본 게시판 상태에서 다른 페이지 보려고 하니 오류가 뜨네.. 흠
    #왜 그냥 기본 상태에서 페이지만 넘기는 상황일 때 위의 if문에서 else가 실행되는게 아니라 if쪽이 실행되는거지
    #페이지 이동을 하려고 숫자 눌렀을 시 search에는 'None' 이 담겨있을텐데 그것 또한 True로 파악하고 if문에서 위의 것이 실행되는 것 같다. 
    # != 'None' 추가하여 해결 완료
    #ㅅㅂ 이번에는 그냥 게시판 처음에 불러오는게 오류뜨네. 이번에도 if문쪽이 실행이 됨. 즉 search라는 변수는 말 그대로 None인데 위의 if문이 실행 
    #해결완료
    
    #다만 검색한 것에 대해 일치하는 결과가 아무것도 없는 경우에 대해서는 오류가 뜰 수도 있겠다. data라는 변수에 [] 로만 담겨있어서 data.page를 할 수도 없을테니
    #이런 경우에 대해서는 더 조정이 필요할 것.


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
        data.view_count += 1
        data.save()   
        #새로고침을 하는 것도 그 페이지를 계속 다시 요청하는 것이므로 조회수가 올라간다. 추천과 비추천을 누른 경우에도 페이지를 redirect하는 것이
        #므로 조회수가 계속 올라간다. 따라서 boardGoodBad 함수에서 조금 조정이 필요
        #아무튼간 게시글을 직접적으로 보고자 할 때 이 함수가 작동이 되고, 그것은 곧 해당 게시물을 보고자 하는거니까 보기 바로 직전에 조회수 하나 올려주고 페이지 던지기
        response = render(request, 'board/view.html', context)
    elif request.method == 'POST':
        response = redirect('board:view', idx)
    return response


def boardUpdate(request):
    if request.method == 'GET':
        data = Board.objects.get(id=request.GET.get('id'))
        context = {
            'forms':BoardForm(initial={'title':data.title, 'content':data.content, 'author':data.author}),
            'data':data
        }
        response = render(request, 'board/update.html', context)
    elif request.method == 'POST':
        data = Board.objects.get(id=request.POST.get('id'))
        data.title = request.POST.get('title')
        data.content = request.POST.get('content')
        #data.author = request.POST.get('author')
        data.save()
        response = redirect('board:view', data.id )
    return response
    #author에 대한 부분에 있어서 나는 update페이지로 넘겨줘야만 함. 선생님은 forms.py에서 required가 없기 때문에 폼을 넘겨주고 넘겨받을 때
    #해당 공간이 비어있어도 된다. 어차피 수정하는 것이고 작성자부분은 바뀌지 않을 것이기 때문에. 
    #근데 나는 required를 넣었었고 이에따라 데이터를 넘겨받을 때 쓰든 안쓰든 해당 부분도 필수적으로 채워져 있었어야 함(채워져 있기만 하면 됨)

def boardDelete(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            data = Board.objects.get(id=request.GET.get('id'))
            if request.user.username == data.author:
                context = {
                    'data':data
                }
                response = render(request, 'board/delete.html', context)
            else:
                return HttpResponse('잘못된 접근')
        else:
            return HttpResponse('잘못된 접근')
#삭제버튼이 게시글 작성자에 대해서만 보이게 한다고 해서 다 되는 것이 아니다. 여전히 다른 사용자나 로그인하지 않은 사용자가
#http://127.0.0.1:8000/board/delete/?id=1/ 과 같이 url GET방식으로 함수에 접근하여 id가 1번인 게시글에 대하여 접근시도를 할 수도 있다. 
#따라서 중요한 것에 대해 처리가 GET방식이라면 URL을 통한 접근부분도 차단을 고려해야 한다.

    elif request.method == 'POST':
        Board.objects.get(id=request.POST.get('id')).delete()
        BoardComment.objects.fileter(board_id=request.POST.get('id')).delete()
        response = redirect('board:index')
    return response




def boardGoodBad(request, idx):
    if request.method == 'GET':
        #로그인한 사용자만 추천 비추천 가능하도록
        if request.user.is_authenticated():
            data = Board.objects.get(id=idx)
            if request.GET.get('type') == 'good':
                data.good_count += 1
            elif request.GET.get('type') == 'bad': #else라고 해도 될 것.
                data.bad_count += 1
            data.view_count -= 1   #추천과 비추천을 누르고 페이지를 redirect하게 되는데 이 때 조회수가 올라가버린다. 따라서 미리 내려놓기
            data.save()
            response=redirect('board:view', idx)
        else: #만약 로그인하지 않은 사용자라면 추천과 비추천버튼을 눌렀을 시 그냥 해당 페이지만 계속 보게만 됨. 아 이때에도 조회수는 올라가겠네.
            response=redirect('board:view', idx)
            #따라서 그냥 아예 추천과 비추천버튼을 눌렀을 시 로그인한 사용자만 가능하다고 만드는게 나을 듯. 자바스크립트 등으로.
    elif request.method == 'POST':
        pass
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