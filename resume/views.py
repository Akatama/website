from django.shortcuts import render
from resume.models import Resume


# Create your views here.
def resume_index(request):
    resume = Resume.objects.get(pk=1)
    context = {
        "resume": resume,
    }
    return render(request, "resume/resume.html", context)
