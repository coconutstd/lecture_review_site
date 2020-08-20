from django.contrib import admin
from .models import Lecture, Teacher,Book

class LectureAdmin(admin.ModelAdmin):
    list_display = ['lecture_title', 'teacher']
    list_display_links = ['lecture_title']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','link']
    list_display_links = ['title']


# Register your models here.
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Teacher)
admin.site.register(Book)