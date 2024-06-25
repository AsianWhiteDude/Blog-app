from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.posts, name='posts'),
    path('generate-blog', views.generate_blog, name='generate_blog'),
]