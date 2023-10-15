from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
        labels = {'username': 'Имя пользователя',
                  'password1': 'Пароль',
                  'password2': 'Подтверждение пароля',
                  'first_name': 'Имя',
                  'last_name': 'Фамилия',
                  'email': 'Почта'}
        widgets = {'username': 'Имя пользователя',
                  'password1': 'Пароль',
                  'password2': 'Подтверждение пароля',
                  'first_name': 'Имя',
                  'last_name': 'Фамилия',
                  'email': 'Почта'}
        