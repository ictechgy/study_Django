from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    start_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(null=True)

class Choices(models.Model):
    q_id = models.IntegerField(null=True)
    text = models.TextField(null=True)
    count = models.IntegerField(default=0)

#models를 다 만든다음에는 makemigrations와 migrate로 데이터베이스에 테이블 생성하는 것 잊지 말기

#Field생성 함수 뒤에는 꼭 괄호는 있어야 하네. count = models.IntegerField 이렇게 하면 테이블 칼럼값 생성 안됨
#게다가 안에 null값을 넣을 수 있게할지 말게할지 등 다 지정해줘야 한다고 경고문이 뜬다.. 