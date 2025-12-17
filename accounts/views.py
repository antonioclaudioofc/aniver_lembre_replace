from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileRegisterForm, LoginForm


def index(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'accounts/index.html')


def register(request):
    if request.method == "POST":
        form = ProfileRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("/")
    else:
        form = ProfileRegisterForm()
    return render(request, 'register/index.html', {"form": form})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.cleaned_data["user"])
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, 'login/index.html', {"form": form})


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('/accounts/login/')


@login_required
def profile(request):
    return render(request, 'profile/index.html', {
        'user': request.user,
    })
