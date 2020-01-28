from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from . import models
import datetime


def home(request):
    return render(request, 'data/home.html', {'activate': 'home'})


#
# Data api view
#
def data(request):
    if request.method == 'POST':
        pass
    else:
        querySet = models.ClientData.objects.all()
        data = list(querySet.values())
        data = [(r['timestamp'].timestamp() * 1000, r['value']) for r in data]
    return JsonResponse(data, safe=False)