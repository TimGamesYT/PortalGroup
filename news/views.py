from django.shortcuts import render

def novations(request):
    return render(request, 'news/novations.html')

def announs(request):
    return render(request, 'news/announs.html')
