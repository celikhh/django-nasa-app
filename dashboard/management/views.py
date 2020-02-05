from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import UpdateView, TemplateView

from dashboard.management.forms import UserPasswordChangeForm
from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserPasswordChangeView(UpdateView):                   #TRY
    model = User
    template_name = "registration/change_password.html"
    form_class = PasswordChangeForm


def change_password(request):      #MAKE CLASS BASED
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

# from django.shortcuts import render, redirect
# from .forms import RegisterForm, LoginForm
# from django.contrib import messages
# from django.contrib.auth.models import User
#
# from django.contrib.auth import login, authenticate, logout, urls
# from django.contrib.auth.decorators import login_required
#
#
# # Create your views here.
#
# def register(request):
#     form = RegisterForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#
#         newUser = User(username=username)
#         newUser.set_password(password)
#
#         newUser.save()
#         login(request, newUser)
#         messages.info(request, "succesfull...")
#
#         return redirect("index")
#     context = {
#         "form": form
#     }
#     return render(request, "register.html", context)
#
#
# def loginUser(request):
#     # import ipdb
#     # ipdb.set_trace()
#     form = LoginForm(request.POST or None)
#
#     context = {
#         "form": form
#     }
#
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#
#         user = authenticate(username=username, password=password)
#
#         if user is None:
#             messages.info(request, "username or passw wrong")
#             return render(request, "login.html", context)
#
#         messages.success(request, "Successful")
#         login(request, user)
#         return redirect("apod")
#     return render(request, "login.html", context)
#
#
# @login_required
# def logoutUser(request):
#     logout(request)
#     messages.success(request, "successful")
#     return redirect("login")
