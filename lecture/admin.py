from django.contrib import admin
from .models import Lecture, Teacher,Book

class LectureAdmin(admin.ModelAdmin):
    list_display = ['lecture_title', 'teacher']
    list_display_links = ['lecture_title']

# Register your models here.
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Teacher)
#admin.site.register(Book)