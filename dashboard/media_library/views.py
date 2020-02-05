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

    # def get_keyword_and_response(self, **kwargs):
    #     keyword = self.kwargs['str']
    #     data = search_media(keyword)
    #     return data

    def get_context_data(self, **kwargs):
        # data = search_media(self.keyword)
        keyword = self.kwargs['str']
        datas = search_media(keyword)
        context = super().get_context_data(**kwargs)
        context['datas'] = datas
        return context
