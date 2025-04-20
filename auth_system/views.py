from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'auth_system/login.html')
def Logout(request):
    logout(request)
    return redirect('/')