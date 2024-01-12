from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# front
def blog(request):
    context = {}
    return render(request, 'front/blog.html', context) 

def categori(request):
    context = {}
    return render(request, 'front/categori.html', context) 

def contact(request):
    context = {}
    return render(request, 'front/contact.html', context) 

def elements(request):
    context = {}
    return render(request, 'front/elements.html', context) 

def index(request):
    context = {}
    return render(request, 'front/index.html', context) 

def all(request):
    context = {}
    return render(request, 'front/all.html', context) 

# def about(request):
#     return render(request, 'front/about.html') 

# def details(request):
#     return render(request, 'front/details.html') 

# def main(request):
#     return render(request, 'front/main.html') 

# def singleblog(request):
#     return render(request, 'front/single-blog.html') 


# dashboard
def dashboard_index(request):
    context = {}
    return render(request, 'dashboard/index.html', context) 