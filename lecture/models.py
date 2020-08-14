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

######DB에 추가해놨음 books #######
class Book(models.Model):
    # book 추천 TAB with 크롤링
    book_title=models.CharField(max_length=100)
    book_author=models.CharField(max_length=20)
    book_price=models.IntegerField()
    book_link=models.CharField(max_length=200)
    book_like=models.CharField(max_length=20,null=True,default='')
######DB에 추가해놨음 books #######n