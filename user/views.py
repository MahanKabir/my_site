from django import forms
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def dashboard(request):
    return render(request, 'admin/dashboard.html')