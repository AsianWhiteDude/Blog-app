
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('sign_up/', views.SignUpUser.as_view(), name='sign_up'),
]