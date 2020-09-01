from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser
from chat.models import nick

class SignupForm(forms.ModelForm):
    c_list = ['MANAGER', 'AI', 'CLOUD', 'BIGDATA', 'IOT']
    CLASS_CHOICES = tuple(enumerate(c_list))
    n_list=nick.objects.values('nick_nickname')
    temp_dict={}

    for idx,i in enumerate(n_list):
        temp_dict[idx]=i['nick_nickname']

    temp_list=[ i for i in temp_dict.values()]

    NICK_CHOICES=tuple(enumerate(temp_list))


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
    nickname = forms.ChoiceField(choices=NICK_CHOICES, widget=forms.Select(
        choices=NICK_CHOICES,
        attrs={
            'class': 'form-control form-control',
            'placeholder': '닉네임',
        }
    ))
    my_class = forms.ChoiceField(choices=CLASS_CHOICES, widget=forms.Select(
        choices=CLASS_CHOICES,
        attrs={
            'class': 'form-control form-control',
            'placeholder': '반선택',
        }
    ))
    # forms.Select(
    #     choices=CLASS_CHOICES,
    #     attrs={
    #         'class': 'form-control form-control-user',
    #         'placeholder': '반선택',
    #     }
    # )
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
        fields = ("email", "name", "nickname", "my_class", "password1", "password2")

        def __init__(self, *args, **kwargs):
            super(SignupForm, self).__init__(*args, **kwargs)
            self.field['my_class'].widget.attrs.update({
                'class': 'form-control form-control-user',
            })


            self.field['email'].widget.attrs.update({
                'class': 'form-control form-control-user',
                'placeholder': 'test'
            })

    def clean_password2(self):
        # TODO : front에서 자바스크립트로도 구현하기
        cd = self.cleaned_data
        print(cd)
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return cd['password2']
