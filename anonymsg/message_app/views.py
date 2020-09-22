from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_message

from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import Message

# Create your views here.


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.create(username=username)
        user_obj.set_password(password)
        user_obj.save()

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('home')


    return render(request, 'signup.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            django_message.info(request, 'Invalid Login Credentials.')

    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def messages(request):
    return render(request, 'messages.html')


def send_message(request, username):
    if request.method == 'POST':
        message = request.POST.get('message')
        try:
            user = User.objects.get(username=username)
            Message.objects.create(user=user, message=message)
            django_message.info(request, f"Message Sent to {username}.")
            return redirect('success')
        except:
            django_message.info(request, "Invalid Target User")

    context = {
    'username': username,
    }

    return render(request, 'send_message.html', context)


def success(request):
    return render(request, 'success.html')
