from django.contrib import admin

# Register your models here.
from htm.models import htmTagTable   #아까 model에서 만든 테이블을 가져오기

#admin.site.register(htmTagTable)  #그냥 이것만 작성해줘도 어드민 사이트에 해당 테이블이 등록되어 보이긴 함
#어드민계정을 통해 데이터베이스의 테이블에 직접 값을 추가 수정 삭제할 수 있도록 해준다.

#http://127.0.0.1:8000/admin 에 들어간 뒤에 우리가 만든 테이블에 들어가자. 그리고 행추가를 함
#정보를 추가하면 htmTagTable Object라고 뜬다. 어떠한 정보인지는 바로 확인이 불가능하다.

class htmTagAdmin(admin.ModelAdmin):
    list_display = (           #리스트를 보여줄 때 어떠한 방식으로 보여줄 것인지 지정
        'id', 'tag_name',    #'' 로 문자로 써야하며 각각의 column명을 기입하여야 한다.
    )
    #이렇게 하면 리스트로 행들이 보여질 때 각각의 칼럼을 미리 볼 수 있다. 즉 테이블에 대해 전체적으로 볼 수 있게 됨
    #원래는 클릭해서 직접 들어가야 어떤 tag_name과 Context인지를 볼 수 있었는데..

admin.site.register(htmTagTable, htmTagAdmin)

#여기에 테이블을 추가 안하면 어드민페이지에서 보이지 않음