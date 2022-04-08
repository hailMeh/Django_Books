from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>INDEX</h1>')


def category(request):
    return HttpResponse('<h1>CATEGORY</h1>')


