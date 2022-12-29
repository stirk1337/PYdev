from django.shortcuts import render
from django.http import HttpResponse


def demand(request):
    return render(request, 'demand/demand.html')