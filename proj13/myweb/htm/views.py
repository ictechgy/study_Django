from django.shortcuts import render, redirect
from htm.models import htmTagTable

# Create your views here.
def mainIndex(request):
    data = htmTagTable.objects.values_list('tag_name', flat=True).all()
    context = {
        'tag_list': data
    }
    return render(request, 'htm/index.html', context)


def htmSearch(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        data = htmTagTable.objects\
               .values('tag_name' ,'tag_context')\
               .get(tag_name=search)
               
        context = {
            'data': data
        }
        return render(request, 'htm/tags.html', context)


def htmTag(request, tag):
    data = htmTagTable.objects\
           .values('id', 'tag_name' ,'tag_context')\
           .get(tag_name=tag)

    context = {
        'data': data
    }

    return render(request, 'htm/tags.html', context)


def htmCalc(request):
    if request.method == 'GET':
        num1 = int(request.GET.get('num1', 0))
        num2 = int(request.GET.get('num2', 0))

        context = {
            'result': num1 + num2
        }

        return render(request, 'htm/calc.html', context)

def htmAdd(request):
    if request.method == 'GET':
        return render(request, 'htm/add.html')
    elif request.method == 'POST':
        name = request.POST.get('tag_name')
        context = request.POST.get('tag_context')
        htmTagTable.objects.create(tag_name=name, tag_context=context)

        return redirect('/htm/')

def htmUpdate(request):
    if request.method == 'GET':
        # DB 수정 할 정보 검색
        data = htmTagTable.objects.get(id=request.GET.get('id'))
        context = {
            'data': data
        }
        return render(request, 'htm/update.html', context)
    elif request.method == 'POST':
        # DB 정보 수정
        # data = htmTagTable.objects.filter(id=request.POST.get('id'))
        # data.update(
        #     tag_name=request.POST.get('tag_name'),
        #     tag_context=request.POST.get('tag_context')
        # )
        # return redirect('/htm/tag/{}/'.format(data[0].tag_name))

        data = htmTagTable.objects.get(id=request.POST.get('id'))
        data.tag_name = request.POST.get('tag_name')
        data.tag_context = request.POST.get('tag_context')
        data.save()
        return redirect('/htm/tag/{}/'.format(data.tag_name))


def htmDelete(request):
    if request.method == 'GET':
        data = htmTagTable.objects.get(id=request.GET.get('id'))
        context = {
            'data': data
        }
        return render(request, 'htm/delete.html', context)
    elif request.method == 'POST':
        htmTagTable.objects.get(id=request.POST.get('id')).delete()
        return redirect('/htm/')