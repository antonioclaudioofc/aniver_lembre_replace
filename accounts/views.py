from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import ProfileRegisterForm, LoginForm


def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    if request.method == "POST":
        form = ProfileRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = ProfileRegisterForm()
    else:
        form = ProfileRegisterForm()
    return render(request, 'register/index.html', {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.cleaned_data["user"])
            return redirect("/")
        else:
            form = LoginForm()
    else:
        form = LoginForm()
    return render(request, 'login/index.html', {"form": form})
