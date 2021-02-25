from django.shortcuts import render
from .models import Job, Intro
# Create your views here.


def homepage(request):
    job_list = Job.objects.all()
    intro_list = Intro.objects.all()
    context = {
        "jobs": job_list,
        "intro": intro_list
    }
    return render(request, 'index.html', context)
