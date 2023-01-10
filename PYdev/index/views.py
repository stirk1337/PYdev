from django.shortcuts import render
from django.http import HttpResponse
from. models import Text, Picture


def index(request):
    data = Text.objects.all()
    img = Picture.objects.all()
    return render(request, 'index/index.html', {'data': data, 'img': img})