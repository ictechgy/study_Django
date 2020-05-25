from django.conf.urls import url

urlpatterns = [

    url(r'^$', 'htm.views.mainIndex'),
    # url(r'^tag/$', 'htm.views.htmTag'),

    #2018-06-20
    url(r'^tag/add/$', 'htm.views.htmAdd', name='add'),
    #아래의 패턴에 들어가지 않게 위에다가 작성해줌
    url(r'^tag/([a-z]+)/$', 'htm.views.htmAdd'),
    
    


    
    #2018-06-18
    url(r'^tag/$', 'htm.views.htmSearch'),
    #실습
    url(r'^calc/$', 'htm.views.htmCalc'),
    url(r'^calc/result/$', 'htm.views.htmResult'),
    #왜 오류나나 했는데 name값 너으니까 오류나네 왜지. name값 넣을거면 다 넣어야하나... 

]