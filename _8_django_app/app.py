'''1.Django App:

In the previous topics, we have seen a procedure to create a Django project.
Now, in this topic, we will create app inside the created project.

Django application consists of project and app, it also generates an automatic base directory for the app,
so we can focus on writing code (business logic) rather than creating app directories.

The difference between a project and app is, a project is a collection of configuration
files and apps whereas the app is a web application which is written to perform business logic.

To create an app, we can use the following command.

$ python3 manage.py startapp appname

2.Django App Example:

$ python3 manage.py startapp myapp

See the directory structure of the created app,
it contains the migrations folder to store migration files and model to write business logic.

Initially, all the files are empty, no code is available but we can use these to
implement business logic on the basis of the MVC design pattern.

To run this application, we need to make some significant changes which display
hello world message on the browser.

Open views.py file in any text editor and write the given code to it
and do the same for urls.py file too.

// views.py

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

// urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
]
We have made changes in two files of the application.
Now, let's run the it by using the following command. This command will start the server at port 8000.

3.Run the Application:

$ python3 manage.py runserver

Open any web browser and enter the URL localhost:8000/hello. It will show the output given below.


'''


