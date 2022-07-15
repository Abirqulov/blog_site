from django.shortcuts import render
from .models import Contact
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


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        contact_post = Contact(name=name, phone=phone, email=email, message=message)
        contact_post.save()

        return render(request, 'contact.html')
