from django.db import models

# Create your models here.
class htmTagTable(models.Model):
    tag_name = models.CharField(max_length=15)
    tag_context = models.TextField()
    