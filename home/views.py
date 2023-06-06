from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def portfolio(request):
 return render(request, 'home/portfolio.html')

def resume(request):
 return render(request, 'home/resume.html')

def blog(request):
 return render(request, 'home/blog-home.html')

def contact(request):
 return render(request, 'home/contact.html')
