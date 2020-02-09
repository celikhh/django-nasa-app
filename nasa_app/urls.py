"""nasa_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import login, views
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from django.urls import path, include, reverse
from django.utils.functional import lazy
from django.views.generic import RedirectView

# from dashboard.management.views import LoginView
from django.contrib import admin
from django.urls import path, include

# login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')
# from dashboard.management.forms import LoginForm

# login_forbidden = user_passes_test(lambda u: u.is_anonymous(), lazy(reverse, str)('home_apod'))

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),         #SESSION CONTROL
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
]
