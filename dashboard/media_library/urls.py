from . import views
from django.urls import path

urlpatterns = [
    path('media_library/<str:str>/', views.MediaLibraryView.as_view(), name='media_library'),
]