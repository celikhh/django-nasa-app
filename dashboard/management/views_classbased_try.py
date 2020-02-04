from django.shortcuts import render

# Create your views here.


from django.views import generic


class LoginView(generic.ListView):
    queryset = ['a', 'b']
    template_name = 'login.html'
    pass


class SignupView(generic.ListView):
    queryset = ['a', 'b']
    template_name = 'signup.html'
    pass


from django.contrib.auth import authenticate, login

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.