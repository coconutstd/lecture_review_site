from django.db import models
from django.utils import timezone

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    # TODO: teacher 정보목록을 참조하여 선택할 수 있도록 추후 모델 수정 필요
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    lecture_title = models.TextField()
    lecture_description = models.CharField(max_length=200)
    # TODO: 추후에 blank, null 처리해줘야함
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.lecture_title

