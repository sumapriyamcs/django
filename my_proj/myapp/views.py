from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# class based based view
# function based view
from django.views import View


def index(request):
    return HttpResponse('Hello suma')

def name(request):
    response = """<p> Hi suma you are in name</p>"""
    return HttpResponse(response)

def game(request, guess):
    response = """<h1> Hi suma you are in
     this page number """ + guess +"""</h1>"""
    return HttpResponse(response)
# first we need to create a view
# we neet to create a route in urls.py
# need to add that route in proj urls.py

# urls --> views --> check data base if we need to store data or retrive
# send data to html --> that file is viewed

# from url we got ynamic --> urls.py --> view.py --> function --> we are accessing
# --> we will process an sen back to fe


def html_route(request):
    return render(request, 'myapp/index.html')
#path('suma/<int: number>
def html_route2(request,number):
    context = {'number': number}
    return render(request,'myapp/main.html', context)

def html_route3(request):
    names = ['suma','priya','baba']
    numbers = [1,3, 2]
    context = {'names':names,'numbers': numbers}
    return render(request, 'myapp/number.html', context)

# View TemplateView ListView APIView
class Class_View(View):
    def get(self,request):
        return HttpResponse('suma in class')
    def post(self,request):
        pass
    def put(self,request):
        pass

# create a function create a class an its methos
# create a template
# route url in urls.py

class Myclass2(View):
    def get(self,request,guess):
        context = {'guess': guess}
        return render(request, 'myapp/block.html', context)