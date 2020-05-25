from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 30)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    good_count = models.IntegerField(default=0)
    bad_count = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True) #생성했을 때에만 자동 추가
    update_date = models.DateTimeField(auto_now=True) #생성 및 수정시에 자동 추가

class BoardComment(models.Model):
    board_id = models.IntegerField()
    author = models.CharField(max_length=30)
    content = models.CharField(max_length=250)
    create_date = models.DateTimeField(auto_now_add=True)

#model 정의한 다음에는 makemigrations 및 migrate 필수!

#일단 데이터베이스의 값이 잘 추가가 되고 함수를 통해 index.html에서 잘 보여지는지 테스트하려면
#데이터베이스 프로그램을 이용하거나 admin사이트에서 데이터베이스에 접근가능하도록 설정하자