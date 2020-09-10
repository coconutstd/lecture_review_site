from django import forms
from .models import Question, Choice
from django.utils import timezone


class QuestionChoiceForm(forms.ModelForm):
    model = Question
    question_text = forms.CharField(required=True)

    class Meta:
        model = Question
        fields = ['question_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args:
            for choice, choice_val in args[0].items():
                if choice.startswith('choice_text_'):
                    self.fields[choice] = forms.CharField(required=True)

    def clean(self):
        choices = list()
        i = 0
        field_name = 'choice_text_%s' % (i,)
        while self.cleaned_data.get(field_name):
            choice_text = self.cleaned_data[field_name]
            if choice_text in choices:
                self.add_error(field_name, 'Duplicate')
            else:
                choices.append(choice_text)
            i += 1
            field_name = 'choice_text_%s' % (i,)
        self.cleaned_data['choices'] = choices

    def save(self, user):
        question = Question(question_text=self.cleaned_data['question_text'], created_date=timezone.now(),
                            deadline_date=timezone.now(), author=user)
        question.save()
        question.choice_set.all().delete()
        for choice in self.cleaned_data['choices']:
            Choice.objects.create(
                question=question,
                choice_text=choice,
            )
        return question
