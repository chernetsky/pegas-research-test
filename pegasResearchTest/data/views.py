from django.shortcuts import render


def home(request):
    return render(request, 'data/home.html')


def about(request):
    return render(request, 'data/about.html')

