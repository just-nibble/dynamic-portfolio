from django.shortcuts import render
from .models import Job
# Create your views here.


def homepage(request):
    job_list = Job.objects.all()
    return render(request, 'index.html', {"jobs": job_list})
