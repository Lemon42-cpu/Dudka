from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = '/board/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('board')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'


    def get_success_url(self):
        return '/board/'

def logout_user(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'main/index.html')