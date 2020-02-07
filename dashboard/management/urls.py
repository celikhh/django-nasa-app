from . import views
from django.urls import path, include

# urlpatterns = [
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('signup/', views.SignupView.as_view(), name='signup'),
# ]

# urlpatterns = [
#     path('register/', views.register, name="register"),
#     path('login/', views.loginUser, name="login"),
#     path('logout/', views.logoutUser, name="logout"),
#
# ]


from django.contrib import admin
from django.urls import path, include  # new


urlpatterns = [
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    # path('accounts/change_password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    # path('password/', views.change_password, name='change_password'),
]
