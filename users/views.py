import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import messages
from .forms import UserRegister

def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} successfully registered")
            return redirect('posts-home')
    else:
        form = UserRegister()
    return render(request, 'users/register.html', {'form':form})


