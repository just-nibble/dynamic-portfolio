from django.shortcuts import render
from .models import Education, Experience, Skill, Hobby
# Create your views here.


def resume(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    hobby = Hobby.objects.all()
    content = {
        'education': education,
        'experience': experience,
        'skill': skill,
        'hobby': hobby,
    }
    return render(
        request, "resume.html", content,
    )
