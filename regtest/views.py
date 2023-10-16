from django.shortcuts import render, redirect
from .form import SignUp
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import generic

def index(req):
    return render(req, 'index.html')


def registration(req):
    if req.POST:
        form = SignUp(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(req, user)
            return redirect('index')
    else:
        form = SignUp()
    return render(req, 'registration/registration.html', context={'regform': form})


class Userlist(generic.ListView):
    model = User

