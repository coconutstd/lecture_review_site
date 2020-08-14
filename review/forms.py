from django import forms

class NewQuestionForm(forms.Form):
    question_text = forms.CharField(label='질문 제목', max_length=100)
