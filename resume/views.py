from django.shortcuts import render
from .models import Education, Experience, Skill, Interests
# Create your views here.


def resume(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    interest = Interests.objects.all()
    content = {
        'education': education,
        'experience': experience,
        'skill': skill,
        'hobby': interest,
    }
    return render(
        request, "resume.html", content,
    )
