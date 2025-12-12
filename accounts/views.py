from django.shortcuts import render, redirect
from .forms import ProfileRegisterForm

# Create your views here.

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
    return render(request, 'register/index.html', {"form": form})
