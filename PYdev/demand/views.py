from django.shortcuts import render
from django.http import HttpResponse
from .models import Demand


def demand(request):
    data = Demand.objects.all()
    return render(request, 'demand/demand.html', {'data': data ,
                                                  'prof': 'Python-программист '})