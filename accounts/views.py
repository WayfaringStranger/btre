from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        return
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
