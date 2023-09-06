from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout

def sign_in(request):
    form = SignInForm(data=request.POST or None)
    if form.is_valid():
       user = form.get_user()
       login(request, user)