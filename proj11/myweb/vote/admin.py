from django.contrib import admin

# Register your models here.
from vote.models import Question, Choices

admin.site.register(Question)
admin.site.register(Choices)
#따로 따로 등록을 진행해야 한다고 하심
#일단 이렇게만 하면 목록상으로 한번에 보는것은 불가능하지만 데이터베이스에 대해 접근은 가능하다.