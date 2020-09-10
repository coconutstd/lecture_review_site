import datetime

from django import forms
from django.db import models
from django.utils import timezone
from myaccount.models import MyUser
from django.conf import settings

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deadline_date = models.DateTimeField()
    is_voting = models.BooleanField(default=True)
    likes_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='likes_user',
    )

    def __str__(self):
        return self.question_text

    def count_likes_user(self):
        return self.likes_user.count()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
