from . import views
from django.urls import path

urlpatterns = [
    path('apod/', views.AstronomyPictureOfTheDayView.as_view(), name='apod'),
]