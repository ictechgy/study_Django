from django.contrib import admin
from vote.models import Question, Choices

# Register your models here.
admin.site.register(Question)
admin.site.register(Choices)
