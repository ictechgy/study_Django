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
    #render로 다른 값을 넘겨줄 때에는 무조건 사전형으로 넘겨줘야한다고 하심. 오류뜨길래 선생님께 질문했는데 그렇게 말씀하심