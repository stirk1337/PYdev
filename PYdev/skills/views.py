from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill, Text


def skills(request):
    skills = Skill.objects.all()
    data = Text.objects.all()
    return render(request, 'skills/skills.html', {'skills': skills, 'data': data})
