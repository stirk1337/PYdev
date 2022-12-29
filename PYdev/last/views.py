from django.shortcuts import render
from django.http import HttpResponse


def last(request):
    return render(request, 'last/last.html')