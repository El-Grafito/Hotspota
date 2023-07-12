from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(
        request,
        'scoop/main.html'
    )

def cat(request):
    return render(
        request,
        'scoop/cat.html'
    )

def info(request):
    return render(
        request,
        'scoop/info.html'
    )
