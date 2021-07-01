import datetime #<- 追記

from django.db import models
from django.utils import timezone #<- 追記

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

class Post2(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


class Player(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    HP = models.TextField()
    point = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

class Card(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    element = models.CharField(max_length=20)
    num = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

