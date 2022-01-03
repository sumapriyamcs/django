'''

1.Django shortcuts module is a collection of helper functions that are generally
used in view function/classes. There are many shortcuts available in module django.shortcuts.
In other words, these function /classes introduce controlled coupling for convenience's sake.

2.render()

It combines a given template with a dictionary and returns the HttpResponse object
with that rendered text. Following is the syntax of the render() function.

Syntax -

render(request, template_name, context=None, content_type=None, status=None, using=None)

Parameters -


Below are the parameters of render() function.

request - It is used to generate the response.
template_name - It takes the template names and display the template contents.

Optional Parameters -

context - It represents the dictionary of values to add to the template context.
content_type - The MIME type to use for the resulting document. Default to 'text/html'.
status - It shows the status code for the response. Defaults to 200.
using - The name of a template engine to use for loading the template.

Example - In the following example, we render the template newapp/index.html.

from django.shortcuts import render
def new_view(request):
    # View code here...
    return render(request, 'newapp/index.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')

It is equivalent to the below code.

def new_view(request):
    # View code here...
    t = loader.get_template('newapp/index.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')

3.redirect()

The redirect() function is used to redirect to the specific URL. It returns an
HttpResponseRedirect to the appropriate URL for the argument passed. Let's see the following syntax.

Syntax -

redirect(to, *args, permanent=False, **kwargs)
Parameters -

A model: The model's get_absolute_url() function will be called.
A view name with arguments: urls.reverse() will be used to reverse-resolve the name.
A URL will be used as-is for the redirect location.

Example -


def blog_view(request, post_id):
    blog = Post.objects.get(pk=post_id)
    return redirect(blog)
    # equivalent to: return HttpResponseRedirect(blog.get_absolute_url())

def blog_view(request, post_id):
    return redirect('blog_details', id=post_id)
    # equivalent to: return HttpResponseRedirect(reverse('blog_details', args=(post_id, )))

def relative_url_view(request):
    return redirect('/blogs/archive/')
    # equivalent to: return HttpResponseRedirect('/blogs/archive/')

By default, the redirect() returns a temporary redirect. However, we can returns
the permanent redirect if set to True.

def my_view(request):
      obj = MyModel.objects.get(...)
   return redirect(obj, permanent=True)

4.get_object_or_404()

It returns the DoesNotExist exception if the searched object is not found.
On the other hand, get() method raise Http404.

Parameters

Klass - A Model class, a Manager, or a QuerySet instance from which to get the object.
**kwargs - Lookup parameters, which should be in the format accepted by get() and filter().
Let's understand the below example.

Example -


from django.shortcuts import get_object_or_404
   def my_view(request):
       obj = get_object_or_404(MyModel, pk=1)
It is equivalent to:

from django.http import Http404
        def my_view(request):
        try:
                obj = MyModel.objects.get(pk=1)
        except MyModel.DoesNotExist:
                raise Http404("No MyModel matches the given query.")
5.get_list_or_404()

It returns the results of filter() on a given model manager cast to a list,
raising Http404 if the resulting list is empty. The syntax is same as get_object_or_404.

Parameters

klass - A Model, Manager or QuerySet instance from which to get the list.
**kwargs - Lookup parameters, which should be in the format accepted by get() and filter().
Let's understand the following example.

Example -

from django.shortcuts import get_list_or_404
def my_view(request):
    my_objects = get_list_or_404(MyModel, published=True)

It is equivalent to:

from django.http import Http404
def my_view(request):
        my_objects = list(MyModel.objects.filter(published=True))
        if not my_objects:
        raise Http404("No MyModel matches the given query.")

We have discussed a few important shortcuts that provide control over the objects.
These shortcuts also allow handling the potential errors effectively.
'''