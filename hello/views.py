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
    
def health_check(request):
    return HttpResponse("OK")

def my_view_1(request):
    """
    A view function for Service 1.
    """
    return HttpResponse("Hello from Service 1!")

def my_view_2(request):
    """
    A view function for Service 2.
    """
    return HttpResponse("Hello from Service 2!")
