'''
1.Django Views
A view is a place where we put our business logic of the application.
The view is a python function which is used to perform some business
logic and return a response to the user. This response can be the HTML
contents of a Web page, or a redirect, or a 404 error.

All the view function are created inside the views.py file of the Django app.

1.1: Django View Simple Example

//views.py

import datetime
# Create your views here.
from django.http import HttpResponse
def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
    return HttpResponse(html)    # rendering the template in HttpResponse

Let's step through the code.

First, we will import DateTime library that provides a method to get current
date and time and HttpResponse class.

Next, we define a view function index that takes HTTP request and respond back.

View calls when gets mapped with URL in urls.py. For example

path('index/', views.index),

2.Returning Errors:

Django provides various built-in error classes that are the subclass
of HttpResponse and use to show error message as HTTP response.
Some classes are listed below.

Class	                                        Description

class HttpResponseNotModified	            It is used to designate that a page hasn't
                                            been modified since the user's last request
                                            (status code 304).

class HttpResponseBadRequest	            It acts just like HttpResponse but uses a 400 status code.

class HttpResponseNotFound	                It acts just like HttpResponse but uses a 404 status code.

class HttpResponseNotAllowed	            It acts just like HttpResponse but uses a 410 status code.

HttpResponseServerError	                    It acts just like HttpResponse but uses a 500 status code.


Django View Example
// views.py

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
def index(request):
    a = 1
    if a:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>') # rendering the template in HttpResponse

3.Django View HTTP Decorators:

HTTP Decorators are used to restrict access to view based on the request method.

These decorators are listed in django.views.decorators.http and return a django.http.HttpResponseNotAllowed if the conditions are not met.

Syntax

require_http_methods(request_method_list)

Django Http Decorator Example

//views.py

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])
def show(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')

This method will execute only if the request is an HTTP GET request.

//urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('show/',  views.show),
]


'''