from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
def index(request):
    a = 1
    if a:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>') # rendering the template in HttpResponse
#from django.shortcuts import render
# Create your views here.
#from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])

def show(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')

import datetime
# Create your views here.
from django.http import HttpResponse
def mcs(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
    return HttpResponse(html)    # rendering the template in HttpResponse
