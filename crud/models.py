from django.db import models


class Lecture(models.Model):
    lecture_title = models.CharField(max_length=30)
    lecture_name = models.CharField(max_length=50)
    lecture_room = models.CharField(max_length=10)

    def __str__(self):
        return self.lecture_title

class Eval(models.Model):
    lect = models.ForeignKey(Lecture, on_delete = models.CASCADE) # lect 외래키 , Lecture모델 객체 삭제-> Eval 객체도 삭제
    title = models.CharField(max_length = 30)
    pub_date = models.DateTimeField('date published')
    text = models.TextField()

    def summary(self):
        return self.text[:50]

