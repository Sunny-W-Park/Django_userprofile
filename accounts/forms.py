from django import forms
from django.core.exceptions import ValidationError

#User registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth

#Import model
from .models import Signup

#<TBD>
#Check duplicate nicknames
#Email auth function should be added

class SignupForm(UserCreationForm):
    username = forms.CharField(
            label = '계정(이메일)',
            max_length = 120,
            widget = forms.TextInput(
                attrs = {
                    "size": "40",
                    }
                )
            )
    password1 = forms.CharField(
            label = '비밀번호',
            widget = forms.PasswordInput(
                attrs = {
                    "placeholder": "한글, 영문, 숫자 조합 8자리 이상",
                    "size": "40",
                    }
                )
            )
    password2 = forms.CharField(
            label = '비밀번호 확인',
            widget = forms.PasswordInput(
                attrs = {
                    "size": "40",
                    }
                )
            )
    name = forms.CharField(
            label = '이름',
            max_length = 120,
            widget = forms.TextInput(
                attrs = {
                    "size": "40",
                    }
                )
            )
    nickname = forms.CharField(
            label = '닉네임',
            max_length = 120,
            widget = forms.TextInput(
                attrs = {
                    "size": "40",
                    }
                )
            )


    def clean_username(self):
        username = self.cleaned_data['username']
        if "@" and ".com" not in username:
            raise ValidationError("유효한 이메일을 입력해주세요.")
        return username

#   def duplicate_username(self):
#       username = self.cleaned_data['username'].lower()
#       r = User.objects.filter(username = username)
#       if r.count():
#           raise  ValidationError("이미 가입된 유저입니다.")
#       return username
#
#   def clean_password(self):
#       password = self.cleaned_data['password1']
#       if len(password) < 8:
#           raise ValidationError("최소 8자리 이상 입력해주세요.")
#       return password





