from django.db import models

# Create your models here.

#htm페이지의 index.html에 있어서 hn, div등 우리는 링크를 만들었었다.
#해당 링크에 대한 태그이름과(div라던지 form이라던지) 누르면 나오는 그 안의 내용에 대해 칼럼 두개로 나누어 만들어보자

class htmTagTable(models.Model):
    tag_name = models.CharField(max_length=15)
    tag_context = models.TextField()

#models.Model은 꼭 기입해야 한다. 상속이라고 해서 부모클래스로부터 부모의 기능과 속성을 이 클래스에서도 그대로 사용할 수 있게끔
#상속받아오는 것임 models.Model은 id의 자동생성에 관한 기능 등 모델에 관한 주요 기능들이 들어가있다.
#원래는 데이터베이스에 연결을 일일히 시켜야 하고 각각의 쿼리문들을 다 만들어줘야 하는데 그러한 기능들이 저기 들어가 있어서 따로 SQL을
#쓰지 않아도 된다. -> 편하군.

#다 작성 한 후에는 migrate로 migration 파일을 만든 뒤 migrate하자
#터미널 기록중 맨 앞의 0001은 로그넘버임. 수정시마다 숫자가 늘어나려나?

#migrations폴더 안에 migrate한 파일이 있음

