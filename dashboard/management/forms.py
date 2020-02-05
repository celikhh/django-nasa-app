from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="username")
    password = forms.CharField(max_length=20, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="confirm", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("not matching")

        values = {
            "username": username,
            "password": password
        }
        return values


class UserPasswordChangeForm(SetPasswordForm):
    username = forms.CharField()

    def save(self):
        user = super(UserPasswordChangeForm, self).save()
        user.username = self.cleaned_data['username']
        user.save()
        return user



