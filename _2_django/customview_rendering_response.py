'''1.Creating the Custom View and Rendering Response:

Steps:
1. Create a file called views.py inside the project folder.
    This is file which is responsible for storing the functions that are responsible
for rendering contents.

To render the response to the http request we need to
import―HttpResponse‖ from django.http.

Syntax:
from django.http import HttpResponse

 To render the response to the http response we need to return the
―HttpResponse‖ with HTML Tags or HTML file.

Syntax:
return HttpResponse(“HTML tags or HTML file”)

2. The function that we write must accept at least an argument to store the request
which comes from the front end.
We prefer to give the name of the argument as ―request‖ only.

3. Ones after writing the function we should do the URL mapping so go to URL‘s.py
file and import the views from the project using the syntax.
Syntax:
from projectname import views

Next the go to the URL patterns variable inside URL‘s.py file
 And set path function is return as
path(“suffix/”, views. Name_of_the function, mapping_name),

4. After that save the all files and run that server (python manage.py runserver), copy
the IP address of that server.

5. Open the browser and paste the IP address like (127.0.0.1:8000/home/) and press
enter, display the HttpResponse of the screen.

In this view, we use HttpResponse to render the HTML (as you have probably
noticed we have the HTML hard coded in the view). To see this view as a page we just need
to map it to a URL.

Now, we want to access that view via a URL. Django has his own way for URL
mapping and it's done by editing your project url.py file (project1/urls.py). The
When a user makes a request for a page on your web app, Django controller takes
over to look for the corresponding view via the urls.py file, and then return the HTML
response or a 404 not found error, if not found. In url.py, the most important thing is
the "urlpatterns" tuple. It‘s where you define the mapping between URLs and views.

Note:
We used HttpResponse to render the HTML in the view before. This is not the best
way to render pages. Django supports the MVT pattern so to make the precedent view,
Django - MVT like, we will need
'''
