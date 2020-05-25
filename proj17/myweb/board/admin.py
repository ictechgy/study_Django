from django.contrib import admin

# Register your models here.
from board.models import Board

admin.site.register(Board)
#그냥 어드민사이트에서 보이도록만 할거면 이정도면 됨. 댓글은 일단 조정은 불가능하지만 게시글부분부터 조정 가능. 보이는 방식이 달라야한다면 class 재정의 필요