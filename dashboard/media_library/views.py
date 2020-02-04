from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import SearchForm
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from ..services import search_media


class MediaLibraryView(LoginRequiredMixin, TemplateView):
    template_name = 'media_library.html'


    def get_keywordd(request):
        form = SearchForm(request.POST or None)
        context = {
            "form": form
        }

        if form.is_valid():
            keyword = form.cleaned_data.get("keyword")

            if keyword is None:
                messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
                return render(request, "home_apod.html", context)
            return keyword
        # return render(request, "login.html", context)


    def get_context_data(self, **kwargs):
        data = search_media(self.keyword)
        context = super().get_context_data(**kwargs)
        context['data'] = self.data
        return context

