from django.shortcuts import render


def home(request):
    return render(request, 'data/home.html', {'activate': 'home'})
