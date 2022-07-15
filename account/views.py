from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib import messages

from .forms import CreateUserForm
from .models import User


def register_page(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Accaunt was created for ' + user)

            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form':form})


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect(reverse('login'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
