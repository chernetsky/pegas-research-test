from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from . import models
import datetime


def home(request):
    return render(request, 'data/home.html', {'activate': 'home'})
