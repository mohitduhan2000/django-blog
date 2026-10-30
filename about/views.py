from django.shortcuts import render
from .models import About

def about(request):
    about_content = About.objects.first()

    context = {
        'about': about_content
    }

    return render(request, 'about/about.html', context)
