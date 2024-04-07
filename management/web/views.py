from django.template import loader
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
def testing(request):
  template = loader.get_template('index.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request)) 