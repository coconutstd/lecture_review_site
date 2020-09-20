from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'modified_date',)

    fieldsets = [
        (None, {'fields': ['question_text', 'author']}),
        ('Date information', {'fields': [readonly_fields]}),

    ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# Register your models here.
