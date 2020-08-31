from django.db import models

class nick(models.Model):
    nick_nickname = models.CharField(max_length=100)
    nick_using=models.BooleanField(default=False)

    def __str__(self):
        return self.nick_nickname