'''
1.Django Static Files Handling:

In a web application, apart from business logic and data handling, we also need
to handle and manage static resources like CSS, JavaScript, images etc.

It is important to manage these resources so that it does not affect our application performance.

Django deals with it very efficiently and provides a convenient manner to use resources.

The django.contrib.staticfiles module helps to manage them.

2.Django Static (CSS, JavaScript, images) Configuration:
 cvb
1. Include the django.contrib.staticfiles in INSTALLED_APPS.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'
]  

2. Define STATIC_URL in settings.py file as given below.

STATIC_URL = '/static/'
3. Load static files in the templates by using the below expression.

{% load static %}

4. Store all images, JavaScript, CSS files in a static folder of the application.
First create a directory static, store the files inside it.


2.Django Image Loading Example:

To load an image in a template file, use the code given below.

// index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
     {% load static %}
</head>
<body>
<img src="{% static '/wallpaper.jpeg' %}" alt="My image" height="300px" width="700px"/>
</body>
</html>


//urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]

//views.py

def index(request):
    return render(request,'index.html')

Run the server by using python manage.py runserver command.

After that access the template by localhost:8000/index URL,and it will produce the
output as a image.

3.Django Loading JavaScript:

To load JavaScript file, just add the following line of code in index.html file.

{% load static %}
   <script src="{% static '/js/script.js' %}"

// index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
     {% load static %}
    <script src="{% static '/js/script.js' %}" type="text/javascript"></script>
</head>
<body>
</body>
</html>

// script.js

alert("Hello, Welcome to Javatpoint");

Run the server by using python manage.py runserver command.
After that access the template by localhost:8000/index URL

4.Django Loading CSS Example:

To, load CSS file, use the following code in index.html file.

{% load static %}
<link href="{% static 'css/style.css' %}" rel="stylesheet">

After that create a directory CSS and file style.css which contains the following code.

// style.css

h1{
color:red;
}

// index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
     {% load static %}
    <link href="{% static 'css/style.css' %}" rel="stylesheet">
</head>
<body>
<h1>Welcome to Javatpoint</h1>
</body>
</html>
Run the server by using python manage.py runserver command.

After that access the template by entering localhost:8000/index URL



'''