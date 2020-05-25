from django.contrib import admin

# Register your models here.    <-- 모델을 여기에 등록하라고 이미 기본 설명이 쓰여져 있다..

from htm.models import htmTagTable   #아까 model에서 만든 테이블을 가져오기

#admin.site.register(htmTagTable)  #그냥 이것만 작성해줘도 어드민 사이트에 해당 테이블이 등록되어 보이긴 함
#어드민계정을 통해 데이터베이스의 테이블에 직접 값을 추가 수정 삭제할 수 있도록 해준다.

#http://127.0.0.1:8000/admin/ 에 들어간 뒤에 admin/admin1234로 로그인 하고, 우리가 만든 테이블에 들어가자. 그리고 데이터 추가를 해보자.
#정보를 추가하고 나와서 리스트를 보면 htmTagTable Object라고 뜬다. 어떠한 정보인지 바로 확인이 불가능하다.
#직접 그 object를 눌러봐야 htmTagTable에서 만들었던 칼럼인 tag_name과 tag_context에 해당하는 값들을 볼 수 있다.
#데이터가 많아져도 일일히 데이터에 직접 들어가야 값을 확인 할 수 있는 구조인데, 이는 매우 불편하다.

#따라서 데이터에 직접 들어가지 않고서도 리스트상에서 데이터들을 일목요연하게 필요한 정보들만이라도 조금 볼 수 있도록 아래와 같이 테이블 보는 방식을 재정의한다.
class htmTagAdmin(admin.ModelAdmin):  #admin클래스에서 모델과 어드민에 관련 된 것을 상속받기?
    list_display = (           #리스트를 보여줄 때 어떠한 방식으로 보여줄 것인지 지정
        'id', 'tag_name',    #'' 로 문자로 써야하며 각각의 column명을 기입하여야 한다. 각각의 칼럼은 쉼표로 구분
    )
    #이렇게 하면 리스트로 테이블의 행들이 보여질 때 각각의 칼럼을 미리 볼 수 있다. 각각의 행에 대한 id값과 tag_name을 미리 볼 수 있음 
    #즉 테이블에 대해 전체적으로 볼 수 있게 됨
    #원래는 클릭해서 직접 들어가야 어떤 tag_name과 Context인지를 볼 수 있었는데..

admin.site.register(htmTagTable, htmTagAdmin)  #기존의 테이블을 등록함과 동시에 내가 재정의한 보기형식 또한 등록하기


#이 파일에서 내가 만들었던 데이터베이스 model 테이블을 추가(register) 안하면 어드민페이지에서 보이지 않음