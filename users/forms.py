from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class SignInForm( AuthenticationForm):
    username = forms.CharField(label='',
         widget=forms.TextInput(attrs={
            'class': 'input', 'placeholder': 'Введите никнейм'
        }))
    
    password =  forms.CharField(label='',
         widget=forms.PasswordInput(attrs={
            'class': 'input', 'placeholder': 'Введите пароль'
        }))
    

    class Meta:
        model = User
        fields = ['usename', 'password']