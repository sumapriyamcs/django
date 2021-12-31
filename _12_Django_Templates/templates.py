'''
1.Django Templates:

Django provides a convenient way to generate dynamic HTML pages by using its template system.

A template consists of static parts of the desired HTML output
as well as some special syntax describing how dynamic content will be inserted.

2.Why Django Template?

In HTML file, we can't write python code because the code is only interpreted
by python interpreter not the browser. We know that HTML is a static markup
language, while Python is a dynamic programming language.

Django template engine is used to separate the design from the python code
and allows us to build dynamic web pages.

3.Django Template Configuration:

To configure the template system, we have to provide some entries in settings.py file.

templates = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
Here, we mentioned that our template directory name is templates.
By default, DjangoTemplates looks for a templates subdirectory in
each of the INSTALLED_APPS.

4.Django Template Simple Example:

First, create a directory templates inside the project app
After that create a template index.html inside the created folder.

5.Loading Template:

To load the template, call get_template() method as we did below and pass template name.
//views.py

from django.shortcuts import render
#importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse
def index(request):
   template = loader.get_template('index.html') # getting our template
   return HttpResponse(template.render())       # rendering the template in HttpResponse

Set a URL to access the template from the browser.

//urls.py

path('index/', views.index),

6.Register app inside the INSTALLED_APPS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'
]

7.Run Server:

Execute the following command and access the template by entering
localhost:8000/index at the browser.

$ python3 manage.py runserver

8.Django Template Language:

Django template uses its own syntax to deal with variable,
tags, expressions etc. A template is rendered with a context which is used
to get value at a web page.

9.Variables:
Variables associated with a context can be accessed by {{}} (double curly braces).
For example, a variable name value is rahul. Then the following statement will
replace name with its value.

My name is {{name}}.
My name is rahul

10.Django Variable Example:

//views.py

from django.shortcuts import render
#importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse
def index(request):
    template = loader.get_template('index.html') # getting our template
    name = {
        'student':'rahul'
    }
    return HttpResponse(template.render(name))       # rendering the template in HttpResponse

//index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
<h2>Welcome to Django!!!</h2>
<h3>My Name is: {{ student }}</h3>
</body>
</html>

11.Tags:

In a template, Tags provide arbitrary logic in the rendering process.
For example, a tag can output content, serve as a control structure e.g.
an "if" statement or a "for" loop, grab content from a database etc.

Tags are surrounded by {% %} braces.
{% csrf_token %}

{% if user.is_authenticated %}
    Hello, {{ user.username }}.
{% endif %}
'''