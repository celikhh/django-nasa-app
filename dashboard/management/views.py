from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.info(request, "succesfull...")

        return redirect("index")
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def loginUser(request):
    # import ipdb
    # ipdb.set_trace()
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "username or passw wrong")
            return render(request, "login.html", context)

        messages.success(request, "Successful")
        login(request, user)
        return redirect("apod")
    return render(request, "login.html", context)


@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, "successful")
    return redirect("login")
