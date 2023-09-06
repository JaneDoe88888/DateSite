from django.shortcuts import render, redirect
from .models import *

def home(request):
    print('hello wolrd')

    

    return render(request, 'home.html', {})