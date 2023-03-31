from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200)
    rank = models.IntegerField()
    content = models.TextField()