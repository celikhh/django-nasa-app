from django.shortcuts import render


# Create your views here.

from django.views import generic


class AstronomyPictureOfTheDayView(generic.ListView):
    queryset = ['a', 'b']
    template_name = 'apod.html'
    pass
