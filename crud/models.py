from django.db import models

#3 모델을 만들어 주어야 makemigrations, migrate 하기
class Lecture(models.Model):
    lecture_title = models.CharField(max_length=30)
    lecture_name = models.CharField(max_length=50)
    lecture_room = models.CharField(max_length=10)
    # admin에 표시하는 방법
    def __str__(self):
        return self.lecture_title

class Eval(models.Model):
    lect = models.ForeignKey(Lecture, on_delete = models.CASCADE) # lect 외래키 , Lecture모델 객체 삭제-> Eval 객체도 삭제
    title = models.CharField(max_length = 30)
    # pub_date = models.DateTimeField('date published')
    created = models.DateTimeField(auto_now_add =True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def summary(self):
        return self.text[:50]

