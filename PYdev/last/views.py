from django.shortcuts import render
from django.http import HttpResponse
from .hh import get_hh_ru


def last(request):
    vacancies = get_hh_ru()
    return render(request, 'last/last.html', {'data': vacancies})