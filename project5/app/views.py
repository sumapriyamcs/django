from django.shortcuts import render
#importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse
def index(request):
   template = loader.get_template('index.html') # getting our template
   return HttpResponse(template.render())       # rendering the template in HttpResponse


#from django.shortcuts import render
#importing loading from django template
#from django.template import loader
# Create your views here.
#from django.http import HttpResponse
def suma(request):
    template = loader.get_template('index1.html') # getting our template
    name = {
        'student':'suma priya puchalapalli'
    }
    return HttpResponse(template.render(name))       # rendering the template in HttpResponse
