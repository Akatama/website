from django.shortcuts import render
from about_me.models import AboutMe


# Create your views here.
def about_view(request):
    about_me = AboutMe.objects.get(pk=1)
    context = {
        "about_me": about_me,
    }
    return render(request, "about_me/about.html", context)
