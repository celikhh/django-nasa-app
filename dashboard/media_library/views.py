from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


from ..services import search_media


class MediaLibraryView(LoginRequiredMixin, TemplateView):
    template_name = 'media_library.html'

    def get_context_data(self, **kwargs):
        keyword = self.kwargs['str']
        datas = search_media(keyword)
        context = super().get_context_data(**kwargs)
        context['datas'] = datas
        return context
