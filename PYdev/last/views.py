from django.shortcuts import render
from django.http import HttpResponse
from .hh import get_hh_ru
from .models import Text


def last(request):
    vacancies = get_hh_ru()
    data = Text.objects.all()
    return render(request, 'last/last.html', {'table': vacancies, 'data': data})
