from django.conf.urls import url

urlpatterns = [

    url(r'^$', 'htm.views.mainIndex'),
    # url(r'^tag/$', 'htm.views.htmTag'),

    #2018-06-20
    url(r'^tag/add/$', 'htm.views.htmAdd', name='add'),
    #아래의 slug패턴에 들어가지 않게 위에다가 작성해줌

    #2018-06-21 수정버튼과 삭제버튼. 역시나 slug패턴에 포함 안되게 그 위에 작성하기
    url(r'^tag/update/$', 'htm.views.htmUpdate'),
    url(r'^tag/delete/$', 'htm.views.htmDelete'),
    #선생님도 나와 동일하게 하긴 했는데 이부분은.. name값을 주긴 함

    

    url(r'^tag/([a-z]+)/$', 'htm.views.htmAdd'),
    
    


    
    #2018-06-18
    url(r'^tag/$', 'htm.views.htmSearch'),
    #실습
    url(r'^calc/$', 'htm.views.htmCalc'),
    url(r'^calc/result/$', 'htm.views.htmResult'),
    #왜 오류나나 했는데 name값 너으니까 오류나네 왜지. name값 넣을거면 다 넣어야하나... 

]