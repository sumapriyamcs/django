from DSEmp.employee_details import Employee
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def methodinfo(request):
    return HttpResponse("Http request is: "+request.method)

def pongal(request):
    return HttpResponse("<h1> i wish you a very happy pongal to everyone<h1>")

def getdata(request):
    data = Employee.objects.get(id=12)
    return HttpResponse(data)

def getdata(request):
    try:
        data = Employee.objects.get(id=12)
    except ObjectDoesNotExist:
        return HttpResponse("Exception: Data not found")
    return HttpResponse(data);
