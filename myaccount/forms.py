from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser

class SignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Email',
        }
    ))
    name = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': '이름',
        }
    ))
    nickname = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': '닉네임'
        }
    ))
    my_class = forms.Select(widget=forms.Select(

    ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Password',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Password confirmation',
            }
        ),
        help_text="Enter the same password as above, for verification."
    )

    class Meta:
        model = MyUser
        fields = ("email", "name", "nickname", "my_class", "password1")

    def clean_re_password(self):
        # TODO : front에서 자바스크립트로도 구현하기
        cd = self.cleaned_data
        if cd['password'] != cd['re_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return cd['re_password']