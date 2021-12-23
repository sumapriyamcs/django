'''
1.Django Cookie:

A cookie is a small piece of information which is stored in the
client browser. It is used to store user's data in a file permanently
(or for the specified time).

Cookie has its expiry date and time and removes automatically when gets
expire. Django provides built-in methods to set and fetch cookie.

The set_cookie() method is used to set a cookie and get() method is used to get the cookie.

The request.COOKIES['key'] array can also be used to get cookie values.

2.Django Cookie Example:

In views.py, two functions setcookie() and getcookie() are used to set and get cookie respectively

// views.py

from django.shortcuts import render
from django.http import HttpResponse

def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response
def getcookie(request):
    tutorial  = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: "+  tutorial);

And URLs specified to access these functions.

// urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('scookie',views.setcookie),
    path('gcookie',views.getcookie)
]

3.Start Server:

$ python3 manage.py runserver

After starting the server, set cookie by using localhost:8000/scookie URL.
It shows the following output to the browser.
And get a cookie by using localhost:8000/gcookie URL. It shows the set cookie to the browser.


'''