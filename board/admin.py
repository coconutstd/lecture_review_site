from django.contrib import admin
from .models import Post_board ,Comment
# Register your models here.

class  PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count_text']
    list_display_links = ['title']

    def count_text(self, obj):
        return '{}글자'.format(len(obj.text))
    count_text.short_description = 'text 글자수' # 이걸 안하면 함수 그대로 나옴

admin.site.register(Post_board, PostAdmin) #임포트한 클래스를 admin사이트에 등록
# 따라서 테이블을 만들 때는 models.py와 admin.py 같이 수정
## 이 방식은 재사용측면에서 유리
admin.site.register(Comment)