from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ваш логин',
        'class': 'text-center my-2 py-2 px-4 rounded-xl bg-gray-100'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ваш пароль',
        'class': 'text-center my-2 py-2 px-4 rounded-xl bg-gray-100'
    }))