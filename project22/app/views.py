from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from random import choice
from django.views.generic.base import RedirectView
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render



# Create your views here.
def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

def post_view(request):
    return redirect('/home/42/')

class SearchRedirectView(RedirectView):
    url = 'https://google.com/?q=%(term)s'


def self(args):
    pass

class RandomAnimalView(RedirectView):
    actor_urls = ['/Chrisevance/', '/Tomhardy/', '/RobertAtinkson/']
    is_permanent = True

    def get_redirect_url(*args, **kwargs):
        return choice(self.actor_urls)

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
            message = form.cleaned_data['message']
            form.save()
            # When the operation is successful, it redirects to another web page.
            return redirect('/success/')

    return render(request, 'contact_form.html', {'form': form})