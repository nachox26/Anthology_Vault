# from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Credenciales incorrectas.')
    return render(request, 'movies/login.html')

@login_required
def index(request):
    return render(request, 'movies/index.html', {'username': request.user.username})

def logout_view(request):
    logout(request)
    return redirect('login')