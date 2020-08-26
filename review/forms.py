from django import forms
from .models import Question


class NewQuestionForm(forms.Form):
    question_text = forms.CharField(label='질문 제목', max_length=100)


class ChoiceForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    choice_text = forms.CharField(label='text', max_length=30)
    votes = forms.IntegerField()
