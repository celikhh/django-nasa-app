from . import views
from django.urls import path

urlpatterns = [
    path('media_library/', views.MediaLibraryView.as_view(), name='media_library'),
]