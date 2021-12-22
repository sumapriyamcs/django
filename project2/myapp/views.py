from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def hello(request):
    return HttpResponse("hello world")
def hello1(request):
    data = """<h1>welcome to pyspider !</h1>"""
    return HttpResponse(data)
def hii(request):
    return HttpResponse("<h1>welcome to mcs !</h1>")