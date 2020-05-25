from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Choices(models.Model):
    q_id = models.IntegerField()
    text = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    