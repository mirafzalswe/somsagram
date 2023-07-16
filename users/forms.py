from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegister(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateProfil(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class UpdateAvatar(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

class UpdateContent(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about']