import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import messages
from .forms import UserRegister, UpdateAvatar, UpdateProfil, UpdateContent
from django.contrib.auth.decorators import login_required
from posts.models import Postlar
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import User


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()  # Сохранение пользователя
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} successfully registered")

            # Проверка существования профиля для данного пользователя
            if not Profile.objects.filter(user=user).exists():
                profile = Profile(user=user)  # Используйте экземпляр User для создания профиля
                profile.save()

            return redirect('users-login')
    else:
        form = UserRegister()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        pic = UpdateAvatar(request.POST, request.FILES, instance=request.user.profile)
        info = UpdateProfil(request.POST, instance=request.user)
        about= UpdateContent(request.POST, request.FILES, instance=request.user.profile)

        if pic.is_valid() and info.is_valid() and about.is_valid():
            pic.save()
            info.save()
            about.save()
            messages.success(request, f"ozgarishalr qabul qilindi")
    else:
        pic = UpdateAvatar(instance=request.user.profile)
        info = UpdateProfil(instance=request.user)
        about = UpdateContent(instance=request.user.profile)
    postlar = Postlar.objects.filter(author=request.user)


    return render(request, 'users/profile.html', {'pic':pic, 'info':info,'about':about, 'postlar':postlar})


@login_required
def update_profile(request):
    if request.method == "POST":
        pic = UpdateAvatar(request.POST, request.FILES, instance=request.user.profile)
        info = UpdateProfil(request.POST, instance=request.user)
        about= UpdateContent(request.POST, request.FILES, instance=request.user.profile)

        if pic.is_valid() and info.is_valid() and about.is_valid():
            pic.save()
            info.save()
            about.save()
            messages.success(request, f"ozgarishalr qabul qilindi")
            return redirect('users-profile')
    else:
        pic = UpdateAvatar(instance=request.user.profile)
        info = UpdateProfil(instance=request.user)
        about = UpdateContent(instance=request.user.profile)
    postlar = Postlar.objects.filter(author=request.user)

    return render(request, 'users/update_profile.html', {'pic':pic, 'info':info,'about':about})


def about(request):
    return render(request, 'users/about.html')

def my_posts(request):
    postlar = Postlar.objects.filter(author=request.user)
    return render(request, 'users/my_posts.html', {'postlar': postlar})