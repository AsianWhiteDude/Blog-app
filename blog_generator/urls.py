from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.all_blogs, name='posts'),
    path('generate-blog', views.generate_blog, name='generate_blog'),
    path('posts/blog-details/<int:pk>/', views.post_details, name='post_details')
]