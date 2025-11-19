from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    return HttpResponse("Yoooo first page")

def second_page(request):
    return HttpResponse("yooo second page")