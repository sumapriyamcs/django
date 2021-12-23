'''
1.Django Request and Response:

The client-server architecture includes two major components request
and response. The Django framework uses client-server architecture to implement web applications.

When a client requests for a resource, a HttpRequest object is created and
correspond view function is called that returns HttpResponse object.

To handle request and response, Django provides HttpRequest and HttpResponse
classes. Each class has it?s own attributes and methods.

Let's have a look at the HttpRequest class.

2.Django HttpRequest:

This class is defined in the django.http module and used to handle the client
request. Following are the attributes of this class.

3.Django HttpRequest Attributes:

Attribute	                                                        Description
HttpRequest.scheme	                    A string representing the scheme of the request (HTTP or HTTPs usually).
HttpRequest.body	                    It returns the raw HTTP request body as a byte string.
HttpRequest.path	                    It returns the full path to the requested page does not include
                                        the scheme or domain.
HttpRequest.path_info	                It shows path info portion of the path.
HttpRequest.method	                    It shows the HTTP method used in the request.
HttpRequest.encoding	                It shows the current encoding used to decode form submission data.
HttpRequest.content_type	            It shows the MIME type of the request, parsed from the CONTENT_TYPE header.
HttpRequest.content_params	            It returns a dictionary of key/value parameters included in
                                        the CONTENT_TYPE header.

HttpRequest.GET	                        It returns a dictionary-like object containing all given HTTP GET parameters.
HttpRequest.POST	                    It is a dictionary-like object containing all given HTTP POST parameters.
HttpRequest.COOKIES	                    It returns all cookies available.
HttpRequest.FILES	                    It contains all uploaded files.
HttpRequest.META	                    It shows all available Http headers.
HttpRequest.resolver_match	            It contains an instance of ResolverMatch representing the resolved URL.

And the following table contains the methods of HttpRequest class.

4.Django HttpRequest Methods:

Attribute	                                                    Description
HttpRequest.get_host()	                        It returns the original host of the request.
HttpRequest.get_port()	                        It returns the originating port of the request.
HttpRequest.get_full_path()                 	It returns the path, plus an appended query string, if applicable.
HttpRequest.build_absolute_uri (location)	    It returns the absolute URI form of location.
HttpRequest.get_signed_cookie (key,
default=RAISE_ERROR, salt='', max_age=None)	    It returns a cookie value for a signed cookie, or raises a django.
                                                core.signing.BadSignature exception if the signature is no
                                                longer valid.

HttpRequest.is_secure()	                        It returns True if the request is secure; that is,
                                                if it was made with HTTPS.

HttpRequest.is_ajax()	                        It returns True if the request was made via an XMLHttpRequest.

5.Django HttpRequest Example:

// views.py

def methodinfo(request):
    return HttpResponse("Http request is: "+request.method)

// urls.py

path('info',views.methodinfo)

Start the server and get access to the browser. It shows the request method name at the browser.

6.Django HttpResponse:

This class is a part of django.http module. It is responsible for generating
response corresponds to the request and back to the client.

This class contains various attributes and methods

7.Django HttpResponse Attributes:

Attribute	                                Description

HttpResponse.content	            A bytestring representing the content, encoded from a string if necessary.
HttpResponse.charset	            It is a string denoting the charset in which the response will be encoded.
HttpResponse.status_code	        It is an HTTP status code for the response.
HttpResponse.reason_phrase	        The HTTP reason phrase for the response.
HttpResponse.streaming	            It is false by default.
HttpResponse.closed	                It is True if the response has been closed.

8.Django HttpResponse Methods:

Method	                                Description

HttpResponse.__init__(content='',
content_type=None, status=200,
reason=None, charset=None)	        It is used to instantiate an HttpResponse object
                                    with the given page content and content type.

HttpResponse.__setitem__
(header, value)	                    It is used to set the given header name to the given value.

HttpResponse.__delitem__(header)	It deletes the header with the given name.

HttpResponse.__getitem__(header)	It returns the value for the given header name.

HttpResponse.has_header(header)	    It returns either True or False based on a
                                    case-insensitive check for a header with the provided name.

HttpResponse.setdefault(header, value)	It is used to set default header.

HttpResponse.write(content)	        It is used to create response object of file-like object.

HttpResponse.flush()	            It is used to flush the response object.

HttpResponse.tell()             	This method makes an HttpResponse instance a file-like object.

HttpResponse.getvalue()	            It is used to get the value of HttpResponse.content.

HttpResponse.readable()	        This method is used to create stream-like object of HttpResponse class.

HttpResponse.seekable()	        It is used to make response object seekable.

We can use these methods and attributes to handle the response in the Django application.
'''