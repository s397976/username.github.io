from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "web/index.html")
def Alaska(request):
    return HttpResponse('hi Alaska')
def greet(request, name):
    return render(request, "web/greet.html",{
        "name" :name.capitalize()
    })
def base (request):
    return render(request,"theme/base.html")