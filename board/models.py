from django.db import models
from django.utils import timezone
from django.conf import settings
from myaccount.models import MyUser

# Create your models here.
class Post_board(models.Model):
    # 작성자
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    # 제목
    title = models.CharField(max_length=200)
    # 내용
    text = models.TextField()
    # 작성일자
    created_date = models.DateTimeField(default=timezone.now)
    # 게시일자
    published_date = models.DateTimeField(blank=True, null=True)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    # 게시일자에 현재날짜시간을 대입해주는 함수
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 객체주소 대신 글 제목을 반환해주는 toString() 함수
    def __str__(self):  # 객체를 문자열로 표현
        return self.title


# Post 에 달리는 댓글 comment 클래스
class Comment(models.Model):
    # post 정보
    postboard = models.ForeignKey('board.Post_board', on_delete=models.CASCADE, related_name='comments')
    # 작성자
    author = models.CharField(max_length=100)
    # author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    # writer = models.CharField(max_length=100)
    # 댓글 내용
    text = models.TextField()
    # 댓글 작성일자
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text


