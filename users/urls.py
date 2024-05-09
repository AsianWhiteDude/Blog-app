
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('login/', views.login_user, name='users:login'),
    path('sign_up/', views.sign_up, name='users:sign_up'),
]