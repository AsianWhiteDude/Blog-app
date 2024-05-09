from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginUserForm

def login_user(request):

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['email'], password=cd['password'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

    form = LoginUserForm()
    return render(request, 'users/login.html', context={'title': 'AI Blog Generator',
                                                                            'form': form})


def sign_up(request):
    return render(request, 'users/sign_up.html', context={'title': 'AI Blog Generator'})

