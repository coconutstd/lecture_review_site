from django.contrib import admin
from .models import Lecture, Eval

# 4 앱 등록
# models에서 모델 만들고 makemigration, migrate하고 나서 admin에 app을 등록해줘야 admin에서 모델 보임
admin.site.register(Lecture)

admin.site.register(Eval)
