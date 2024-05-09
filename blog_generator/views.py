from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, 'blog_generator/index.html', context={'title': 'AI Blog Generator'})


def posts(request):
    return render(request, 'blog_generator/posts.html', context={'title': 'AI Blog Generator'})
