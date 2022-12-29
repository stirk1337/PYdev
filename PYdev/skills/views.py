from django.shortcuts import render
from django.http import HttpResponse


def skills(request):
    return render(request, 'skills/skills.html')