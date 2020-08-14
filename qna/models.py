from django.db import models

# Create your models here.


class Qna(models.Model):

    q_title=models.CharField(max_length=20)
    q_like=models.IntegerField()
    q_text=models.TextField()
    q_author=models.CharField(max_length=20)

    q_start_date = models.DateTimeField(blank=True, null=True)
    q_end_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.q_title
    # TODO
    # 코멘트, 작성자(참조키), like도 참조키로

