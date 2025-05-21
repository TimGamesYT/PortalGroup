from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm
from forum.models import Post

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            
            return redirect('novations')
        else:
            messages.error(request, "Неправильне ім'я користувача або пароль")

    return render(request, 'auth_system/login.html')

def logout_view(request):
    logout(request)

    return redirect('novations') 

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('novations')
    else:
        form = RegistrationForm()
    return render(request, 'auth_system/register.html', {'form': form})

def portfolio(request):
    my_posts = Post.objects.filter(author=request.user)
    avatar = 'profile/default_avatar.png'
    context = {
        'my_posts': my_posts,
        'photo': avatar,
        'user': request.user,
    }
    return render(request, 'auth_system/portfolio.html', context)
