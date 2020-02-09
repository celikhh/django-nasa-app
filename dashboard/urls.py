from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('dashboard.apod.urls')),
    path('', include('dashboard.management.urls')),
    path('', include('dashboard.media_library.urls')),
]