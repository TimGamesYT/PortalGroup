from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm
from forum.models import Post


def homepage(request):
    return render(request, 'homepage.html')

def novations(request):
    return render(request, 'novations.html')

def announs(request):
    return render(request, 'announs.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            
            return redirect('homepage')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'auth_system/login.html')

def logout_view(request):
    logout(request)


    return redirect('homepage') 
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password == password_confirm:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Registration successful")
            return redirect('login') 
        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'auth_system/register.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'auth_system/register.html', {'form': form})

def portfolio(request):
    my_posts = Post.objects.filter(author=request.user)
    avatar = None
    context = {
        'my_posts': my_posts,
        'photo': avatar
    }
    return render(request, 'auth_system/portfolio.html', context)
