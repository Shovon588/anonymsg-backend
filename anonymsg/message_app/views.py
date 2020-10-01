from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_message
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Message

from random import randint

# Create your views here.


@login_required
def home(request):
    message_count = len(Message.objects.filter(user=request.user))
    return render(request, 'home.html', {'message_count': message_count})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        username = username.lower()

        try:
            User.objects.get(username=username)
            django_message.info(request, f"{username} is already taken.")
        except:
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
        username = username.lower()
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
    messages = Message.objects.filter(user=request.user).order_by('-time')
    pagi = Paginator(messages, 4)
    page_number = request.GET.get('page')
    page_obj = pagi.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'messages.html', context)


def favorite_messages(request):
    messages = Message.objects.filter(user=request.user, favorite=True).order_by('-time')
    pagi = Paginator(messages, 4)
    page_number = request.GET.get('page')
    page_obj = pagi.get_page(page_number)

    context = {
        'page_obj': page_obj
}

    return render(request, 'favorite_messages.html', context)


def send_message(request, username):
    if username == request.user.username:
        return redirect('home')

    if request.method == 'POST':
        message = request.POST.get('message')
        try:
            user = User.objects.get(username=username)
            Message.objects.create(user=user, message=message, type="anonymous")
            django_message.info(request, f"You just twinged {username}.")
            return redirect('success')
        except:
            django_message.info(request, "Invalid Target User")

    context = {
    'username': username,
    }

    return render(request, 'send_message.html', context)


def success(request):
    return render(request, 'success.html')


def random_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        users = User.objects.all()
        random_index = randint(0, len(users)-1)
        user = users[random_index]

        if user==request.user:
            if random_index == 0:
                user = users[random_index + 1]
            else:
                user = users[random_index - 1]

        Message.objects.create(user=user, message=message, type="random")
        django_message.info(request, "Message sent to a random user.")
        return redirect('success')

    return render(request, 'random_message.html')


@login_required
def delete_message(request, id):
    if request.method == "POST":
        message = Message.objects.get(id=id)
        message.delete()
        django_message.info(request, "Message Deleted.")
        return redirect('messages')
    return render(request, 'confirm_delete.html')


class ToggleFavorite(APIView):
    def get(self, request, id):
        message = Message.objects.get(id=id)
        if message.favorite:
            print("yeah bitch")
            message.favorite = False
        else:
            message.favorite = True
        message.save()


        return Response({"message": "Toggle Successful"})
