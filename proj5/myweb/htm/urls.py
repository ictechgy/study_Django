from django.conf.urls import url

urlpatterns = [

    url(r'^$', 'htm.views.mainIndex'),
    # url(r'^tag/$', 'htm.views.htmTag'),
    url(r'^tag/([a-z]+)/$', 'htm.views.htmAdd'),
    
    


    
    #2018-06-18
    url(r'^tag/$', 'htm.views.htmSearch'),


    #실습
    url(r'^calc/$', 'htm.views.htmCalc'),
    url(r'^calc/result/$', 'htm.views.htmResult'),
    #왜 오류나나 했는데 name값 넣으니까 오류나네 왜지. name값 넣을거면 다 넣어야하나...  흠?

]