from django import forms
from .models import Post_board, Comment

#Validator 함수 정의
#title 입력필드의 길이 체크<3
def min_length_3_validator(value):
    if len(value) <3:
        raise forms.ValidationError('title 은 3글자 이상 입력해 주세요!')

# PostForm 클래스 선언
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    text = forms.CharField(widget= forms.Textarea)
    def save(self, commit=True):
        post = Post_board(**self.cleaned_data)
        if commit:
            post.save()
        return post

#ModelForm을 상속받는 CommentModelForm 클래스 선언
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', )