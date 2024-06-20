from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, SignUpUserLogin


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'AI Blog Generator'}

    def get_success_url(self):
        return reverse_lazy('home')


class SignUpUser(CreateView):
    form_class = SignUpUserLogin
    template_name = 'users/sign_up.html'
    extra_context = {'title': 'AI Blog Generator'}

    def get_success_url(self):
        return reverse_lazy('users:login')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))