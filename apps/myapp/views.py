from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def our_classes_page(request):
    return render(request, 'glasses.html')


def shop_page(request):
    return render(request, 'shop.html')


def contact_page(request):
    return render(request, 'contact.html')

