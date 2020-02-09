from django.contrib.auth.mixins import LoginRequiredMixin

from ..services import get_picture_of_the_day
from django.views.generic import TemplateView


class AstronomyPictureOfTheDayView(LoginRequiredMixin, TemplateView):
    template_name = 'home_apod.html'
    data = get_picture_of_the_day()              #CHECK

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apod'] = self.data
        return context






