from django.shortcuts import render
from .form import SignUp


def index(req):
    return render(req, 'index.html')


def registration(req):
    form = SignUp()
    return render(req, 'account/registration.html', context={'regform': form})
