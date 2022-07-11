from django.contrib import admin
from django.urls import path
from account.views import *
from apps.myapp.views import home_page

urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('', home_page, name='home'),
    path('logout/', logout_user, name='logout'),

    # myapp


]