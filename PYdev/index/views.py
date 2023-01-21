from django.shortcuts import render
from .models import Text


def index(request):
    data = Text.objects.all()
    return render(request, 'index/index.html', {'data': data, })