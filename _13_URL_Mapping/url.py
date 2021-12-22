'''
1.Since Django is a web application framework, it gets user requests by URL
locater and responds back. To handle URL, django.urls module is used by the framework.

Let's open the file urls.py of the project and see the what it looks like

// urls.py:

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

See, Django already has mentioned a URL here for the admin.
The path function takes the first argument as a route of string or regex type.

The view argument is a view function which is used to return a response (template) to the user.

The django.urls module contains various functions, path(route,view,kwargs,name)
is one of those which is used to map the URL and call the specified view.

2.Django URL Functions:

Here, we are giving some commonly used functions for URL handling and mapping.

Name	                    Description	                            Example

1.path(route, view,
kwargs=None, name=None)	    It returns an element for
                            inclusion in urlpatterns.	        path('index/', views.index,
                                                                name='main-view')


2.re_path(route, view,
kwargs=None, name=None)	    It returns an element for
                            inclusion in urlpatterns.	        re_path(r'^index/$', views.index,
                                                                name='index'),

3.include(module,
namespace=None)	            It is a function that takes a
                            full Python import path to another
                            URLconf module that should be
                            "included" in this place.

4.register_converter
(converter, type_name)	    It is used for registering a converter
                            for use in path() routes.

Let's see an example that gets user request and map that route to call
specified view function. Have a look at the steps.

1. Create a function hello in the views.py file. This function will
be mapped from the url.py file.

// views.py

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])
def hello(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')

// urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/',  views.hello),
]

Now, start the server and enter localhost:8000/hello to the browser.
This URL will be mapped into the list of URLs and then call the corresponding
function from the views file.

In this example, hello will be mapped and call hello function from the views
file. It is called URL mapping.


'''