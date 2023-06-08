from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonalInfo, Skill, Testimonial

def index(request):
    personal_info = PersonalInfo.objects.first()
    testimonials = Testimonial.objects.all()

    skills_languages = Skill.objects.filter(category='LANG').values()
    skills_frameworks = Skill.objects.filter(category='FRAME').values()
    skills_data = Skill.objects.filter(category='DATA').values()
    skills_tools = Skill.objects.filter(category='TOOL').values()
    skills_testing = Skill.objects.filter(category='TEST').values()
    
    context = {
      'personal_info': personal_info,
      'testimonials': testimonials,
      'skills_languages': skills_languages,
      'skills_frameworks': skills_frameworks,
      'skills_data': skills_data,
      'skills_tools': skills_tools,
      'skills_testing': skills_testing,
    }
    return render(request, 'home/index.html', context)

def portfolio(request):
 return render(request, 'home/portfolio.html')

def resume(request):
 return render(request, 'home/resume.html')

def blog(request):
 return render(request, 'home/blog-home.html')

def contact(request):
 return render(request, 'home/contact.html')
