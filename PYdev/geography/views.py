from django.shortcuts import render
from django.http import HttpResponse


def geography(request):
    return render(request, 'geography/geography.html')