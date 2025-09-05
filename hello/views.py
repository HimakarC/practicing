from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hi this is Himakar')

def add(request):
    a = request.GET["n1"]
    b = request.GET["n2"]
    c = int(a) + int(b)
    return render(request, "resut.html", {'result': c})

def bring(request):
    a = 'Hi '
    b = request.GET["name"]
    c = a + b
    return render(request, "n.html", {'Name': c})
