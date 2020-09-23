import datetime

from django import forms
from django.db import models
from django.utils import timezone
from myaccount.models import MyUser
from django.conf import settings


class Timer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    start_time= models.DateTimeField()
    end_time = models.DateTimeField()
