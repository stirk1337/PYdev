from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill


def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skills.html', {'skills': skills})
