'''
1.Django Middleware:

In Django, middleware is a lightweight plugin that processes during request
and response execution. Middleware is used to perform a function in the application.
The functions can be a security, session, csrf protection, authentication etc.

Django provides various built-in middleware and also allows us to write our own
middleware. See, settings.py file of Django project that contains various middleware,
that is used to provides functionalities to the application. For example,
Security Middleware is used to maintain the security of the application.

// settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

2.Creating Own Middleware:

middleware is a class that takes an argument get_response and returns a response.

3.class FirstMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
__init__(get_response)

It must accept the get_response argument because Django
initializes middleware with only it. It calls only once whereas __call__
executes for each request.

Activating Middleware
To activate middleware, add it to the MIDDLEWARE list of the settings.py file.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XframeOptionsMiddleware',
  'add new created middleware here'
]

A Django project does not require middleware, the MIDDLEWARE list can be
empty but recommended that have at least a CommonMiddleware.

3.Middleware Order and Layering:

Middleware applies in the order it is defined in MIDDLEWARE list and each
middleware class is a layer. The MIDDLEWARE list is like an
onion so each request passes through from top to bottom and response is in
reverse order (bottom to up).

4.Other Middleware Methods:

Apart from request and response, we can add three more methods to add more features to our middleware.

process_view(request, view_func, view_args, view_kwargs )

It takes HttpRequest object, function object, list of arguments
passed to the view or a dictionary of arguments respectively.

This method executes just before the calling of view. It returns either None
or HttpResponse, if it returns an HttpResponse, it stops processing and return the result.

process_template_response(request,response)

It takes two arguments first is a reference of HttpRequest and second is
HttpResponse object. This method is called just after the view finished execution.

It returns a response object which implements the render method.

process_exception(request, exception)

This method takes two arguments, first is HttpRequest object and second
is Exception class object that is raised by the view function.

This method returns either None or HttpResponse object. If it returns a response,
the middleware will be applied and the result
returns to the browser. Otherwise, the exception is handle by default handling system.


'''