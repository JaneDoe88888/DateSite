from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from .forms import SignInForm

def home(request):
    action = request.GET.get('action')
    confirm_login = False
    if action == 'log_in':
        confirm_login = True
    form = SignInForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('head:str')
    return render(request, 'home.html', {'form': form, 'confirm_login': confirm_login})

def strr(request):
    return render(request, 'str.html', {})

def sign_out(request):
    logout(request)
    return redirect('head:home')