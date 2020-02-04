from . import views
from django.urls import path

# urlpatterns = [
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('signup/', views.SignupView.as_view(), name='signup'),
# ]

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),

]
