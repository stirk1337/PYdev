from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture, Salary, Proportion


def geography(request):
    data = Salary.objects.all()
    data1 = Proportion.objects.all()
    img = Picture.objects.all()
    return render(request, 'geography/geography.html', {'data': data, 'data1': data1, 'img': img, 'prof': 'Python-программист'})
