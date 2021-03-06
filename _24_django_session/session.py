'''
1.Django Session:

A session is a mechanism to store information on the server side during the
interaction with the web application.

In Django, by default session stores in the database and also allows file-based
and cache based sessions. It is implemented via a piece of middleware and can
be enabled by using the following code.

Put django.contrib.sessions.middleware.SessionMiddleware in MIDDLEWARE and
django.contrib.sessions in INSTALLED_APPS of settings.py file.

To set and get the session in views, we can use request.session and can set multiple times too.

The class backends.base.SessionBase is a base class of all session objects.
It contains the following standard methods.

Method	                                                    Description

__getitem__(key)	                            It is used to get session value.
__setitem__(key, value)	                        It is used to set session value.
__delitem__(key)	                            It is used to delete session object.
__contains__(key)	                            It checks whether the container contains the
                                                particular session object or not.

get(key, default=None)	                        It is used to get session value of the specified key.

Let's see an example in which we will set and get session values.
Two functions are defined in the views.py file.

2.Django Session Example:

The first function is used to set and the second is used to get session values.

//views.py

from django.shortcuts import render
from django.http import HttpResponse

def setsession(request):
    request.session['sname'] = 'irfan'
    request.session['semail'] = 'irfan.sssit@gmail.com'
    return HttpResponse("session is set")
def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname+" "+studentemail);

Url mapping to call both the functions.

// urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('ssession',views.setsession),
    path('gsession',views.getsession)
]

3.Run Server:


$ python3 manage.py runserver

And set the session by using localhost:8000/ssession
The session has been set, to check it, use localhost:8000/gsession



'''