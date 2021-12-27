'''
1.Django Redirects | Complete Guide of Redirects:

In this tutorial, we will one of the important Django concepts redirect.
We will learn about the Django redirects and their uses. We will also see the
example of Redirects and will discuss the permanent and temporary redirects.
We assume that you have already familiar with the basic building concept of Django,
like views, models, and URL patterns. If you are not familiar with Django,
then visit our Django tutorial.

2.What are Redirects?:

When we create a web application using Django framework, we will at some point
where we need to visit one URL to another. We can easily jump from current URL
to another URL by returning an instance of HttpResponseRedirect or
HttpResponseRedirect from our view in django. We need to import the redirect
function using the django.shortcuts module in our view.py file. Let's see the following example.

Example - view.py

# views.py
from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

In the above view.py file, we import the redirect() function and call with a
URL in the view. It will return the HttpResponseRedirect class, which we then
return from our view.

This redirect_view must be included in the url.py file.

# urls.py
from django.urls import path

from .views import redirect_view

urlpatterns = [
    path('/redirect/', redirect_view)

]

Suppose this is the main url.py file of our Django project;
the URL /redirects/ now redirects the /redirect-success/.

There is another way to redirect the URLs. We can use the redirect()
function with the name of the view or URL to avoid the hard-coding style.

3.Why Redirects Useful?

Someone might wonder why we use redirect when we redirect the URL.
To understand where the redirects make sense, read the following important
points regarding the redirects.

Redirects are useful when the user is not logged in and requests a URL that
required authentication to redirect the user to the login page.
When the user logs in successfully, Django redirects the user to the original request.
When the user changes the password, we can redirect the page that shows
the password has changed successfully.

When you create an object in the Django admin, Django redirects you to the object list.

Apart from that, Django Redirects plays an essential role in providing the
direction to the user by the web application. Performing the operations like
creating or deleting the object may create some inconvenience in the application.
Use of redirect can prevent the accidently operating twice.

4.Form handing Example of Redirect:

In the below example, we will use the redirect() function in the form handling,
when the user submitting the form successfully. Let's understand the following code.

Example -

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

def contact_form_handle(request):
    if request.method == 'GET':
        form = ContactForm()
    # The request method 'POST' indicates
    # that the form was submitted
    if request.method == 'POST':  # 1
    # We are creating a form instanse to save the form data
        form = ContactForm(request.POST)  # 2
        # Validate the form
        if form.is_valid():
            # if the submitted data is valid
            # the perform the following operations

            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            mobile = form.cleaned_data['mobile'],
            message =  form.cleaned_data['message']
            form.save()
            # When the operation is successful, it redirects to another web page.
            return redirect('/success/')

    return render(request, 'contact_form.html', {'form': form})

The above code will display and handle the contact form. We can send the data
to template file as well. Let's understand the code in detail.

First, we have imported the form module and we create a form which includes some fields.

Then, we have created the contant_handle_form() function which handle the form.

The view looks at the request method. When the user enters the URL that is
connected to view, the browser performs the GET operation. Basically GET
request serve the data to user.

We checked if a request is POST, we instantiate a ContactForm
If the form is valid, we cleaned the input data using the cleaned_data
After saving the data, the view returns a redirect to the URL /success/.
This is the step that we concern about.

In the next step, We pass the instance of ContactForm and uses django.shortcuts.render()
render the html template.

Note - In Django, the form is created in the forms.py but we create the form
in view.py file to demonstrate how to handle the form.


5.How an HTTP Redirect Works?

Now, here is the questions, how do HTTP redirect works. In this section,
we will learn what happen when user enters a URL in the address bar on their browser.

Suppose we have created a Django application with the "HelloWorld" view that
handles the path /hello/. When we run the web application on the server, the
complete URL will be http://127.0.0.1:8000/hello/.

In the URL, 127.0.0.1 is IP address and 8000 is a port. We send the GET
request for the path /hello/. The server returns the HTTP response.

We can use the curl command with the -include option to look the client and server activity.

$ curl --include http://127.0.0.1:8000/hello/
HTTP/1.1 200 OK
Date: Sun, 09 Jul 2021 02:32:55 GMT
Server: WSGIServer/0.2 CPython/3.6.3
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 11

Hello World

In the first line, HTTP response returns the status code
200 and status message. The status line is followed by an arbitrary number of HTTP headers.

6.Temporary vs. Permanent Redirect:

There are two types of redirects - Temporary and Permanent. The status code
301 represents Permanent Redirect and 302 found. The found indicates a temporary
redirect which means, "The URL you are looking for currently can be found another
address." It is the same as "Our shop is currently closed. Please visit to other store".


The permanent redirect represents that "The URL you are looking is no longer
available at this address. It is available on the new address." The permanent
URL makes the change permanently.

The browser saves the URL response in the cache. Next time the user enters
the same URL, the browser remembers the redirect and redirect requests to the new address.

The permanent and temporary URL is relevant for search engine optimization.

7.The redirect() Function:

We have shown the use of the redirect() function earlier. We can call this
method with a get_absolute_url() method, A URL or view name, and positional and /or keyword arguments.

To make the permanent URL, we need to pass the argument permanent=True,
and it will return an instance of HttpResponsePermanentRedirect.

Example -

from django.shortcuts import redirect

def post_view(request):
    return redirect('/home/42/')

The redirect() function will treat any string a /or .as a URL and use it as redirect target.

8.The RedirectView Class-Based View:

Suppose we have the view that has no use but returning a redirect.
In that case, we can use the class-based view django.view.generic.base.RedirectView.

In the following example, string formatting placeholders are swapped with
the named arguments from the URL.

Example - view.py

from django.views.generic.base import RedirectView

class SearchRedirectView(RedirectView):
  url = 'https://google.com/?q=%(term)s'

Example - urls.py

from django.urls import path
from .views import SearchRedirectView

urlpatterns = [
    path('/search/<term>/', SearchRedirectView.as_view())
]

The URL define with the <term>, which will help to build redirect.
Suppose we search Tom Hardy, the path will be https://google.com/?q=TomHardy.
We pass the keyword argument url to as_view() in the urlpatterns.

urls.py

from django.views.generic.base import RedirectView

urlpatterns = [
    path('/search/<term>/',
         RedirectView.as_view(url='https://google.com/?q=%(term)s')),
]

We can create the dynamic URL by overwriting the get_redirect_url() method.

view.py

from random import choice
from django.views.generic.base import RedirectView

class RandomAnimalView(RedirectView):

     actor_urls = ['/Chrisevance/', '/Tomhardy/', '/RobertAtinkson/']
     is_permanent = True

     def get_redirect_url(*args, **kwargs):
        return choice(self.actor_urls)

The above class-based view redirect to the URL picked randomly from .actor_urls.

This tutorial included the guide on HTTP redirects with Django. We have
explored each important concept of redirects from the low-level detail to
high-level detail of HTTP protocols. We explained permanent and temporary
redirects, class-based redirects. Moreover, the knowledge about redirect is
not only limited to the Django framework; it can be used for web development in any language.

'''