
from django import views
from django.urls import path
from .views import *

# užkrauna puslapį
urlpatterns = [
    path('', index, name='index'),
    path('info/', info, name='info'),
    path('authors/', authors, name='authors'),
    path('login/', login, name='login'),
    path('logged_out/', logged_out, name='logged_out'),
    path('register/', register, name='register'),
    path('password_reset/', password_reset, name='password_reset'),
    path('search/', search, name='search'),
]
