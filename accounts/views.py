from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        return
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    return redirect('index')


def logout(request):
    return render(request, 'accounts/logout.html')
