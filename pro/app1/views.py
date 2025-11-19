

from django.http import HttpResponse
from django.shortcuts import render

#class based views

#function based views

# def home(request):
#     return HttpResponse("Welcome To Django")
#
# def index(request):
#     return HttpResponse("index page")
#
# def new(request):
#     return HttpResponse("hii get lost")

def home(request):
    context={'name':'Arun','age':25}
    return render(request,'home.html',context)

def index(request):
    return render(request,'index.html')
