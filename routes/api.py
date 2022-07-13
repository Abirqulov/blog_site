from django.contrib import admin
from django.urls import path
from account.views import *
from apps.myapp.views import home_page, about_page, our_classes_page, contact_page, shop_page

urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('', home_page, name='home'),
    path('logout/', logout_user, name='logout'),

    # myapp

    path('about/', about_page, name='about'),
    path('classes/', our_classes_page, name='glasses'),
    path('shop/', shop_page, name='shop'),
    path('contact', contact_page, name='contact')

]