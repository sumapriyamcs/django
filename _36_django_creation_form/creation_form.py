'''
1.Django UserCreationForm| Creating New User:

Django comes with a build-in user authentication system. This configuration
performs the most common requirements project needs, handling a wide range of
tasks, and valid passwords and permissions.

We can create the user login by importing user authentication modules.
This article will discuss about the UserCreationForm, which is used to create
a new user. It is a build-in module inherits from the ModelForm class.
Before learning the Django UserCreationForm, let's have a brief introduction of User.

2.What are User objects?

User objects are the main component of the user authentication system.
They are represented as the site visitor and are used to enables thing like
preventing access, registering user profiles, correlating content with creators,
and many more. But the 'superuser' and 'admin' class user objects are provided
the special attributes.

User objects consist of the following primary attributes.

1.username
2.password
3.Email
4.first_name
5.last_name

3.Implement Django UserCreationForm:

Django
UserCreationForm is used for creating a new user that can use our web application.
It has three fields: username, password1, and password2(which is basically
used for password confirmation).

To use the UserCreationForm, we need to import it from django.contrib.auth.forms.

from django.contrib.auth.forms import UserCreationForm
Here, we will create the view to handle the request.

view.py file

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.POST == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
    messages.success(request, 'Account created successfully')

    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

Now we will create the path in Helllo.url.py to handle the request.

from django.urls import path
from django.contrib import admin
from sampleapp.views import register


urlpatterns = [
   path('admin/', admin.site.urls),
    path('register', register, name = 'register')
]

template/base.html

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Register Page</title>
  </head>
  <body>
  {% block content %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>


    {% endblock content %}
  </body>
</html>


Next, we will create the register.html file by extending the base.html file
in template folder.

template/register.html

{% extends 'base.html' %}

{% block content %}

<div class = "login">

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
        </ul>
    {% endif %}

    <h1>Register Here - JavaTpoint Blog</h1>

         <form method="post" >
             {% csrf_token %}
             <table>
                {{ form.as_table }}
                 <tr>
                    <td></td>
                    <td><input type="submit" name="submit" value="Register" /></td>
                </tr>
             </table>
         </form>
     </div>

{% endblock content %}

When we send the request using http://127.0.0.1:8000/register/

When we click on the Register button, the POST request will be generated and
create the new User. The newly created User using UserCreationForm() will set
is_superuser and is_staff as False but is_active set to True.

The UserCreationForm() provides the limited fields. Suppose we want to
send the verification mail to verify the User; we cannot do that because
it doesn't have an email field.

A proper user registration form should take the following steps.

The user fills in their details and hits submit button.
The sites send the verification link on submitted mail.
The user receives the verification link on their entered mail.
To do that, either we modify the UserCreationForm, including the email field
and verification facility, or create a new user registration form from scratch.

We will create the new user registration form because it will provide complete
control over the form.

Now, we will create the forms.py file and create the new class CustomUserCreationForm
in sampleapp's forms.py file.


Example -

\python_project\Myfirstdjangoproject\Hello\sampleapp\forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username = username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit = True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

In the above code, we define four fields name username, email, password1 and
password2 in CustomUserCreationForm. Next, we define individual method for each
field to clean the data. If you look closely, the widget field is used in both
password1 and password2 fields. The widget key argument allows to change the
default widget of the fields.

The username_clean() will prevent to enter duplicate username.
The email_clean() will prevent to enter duplicate email.
The clean_password2() method will check both passwords are matched or not
And then, the save() method will save the data.

Now, we update the register() view in views.py file.

from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
# Create your views here.

def register(request):
    if request.POST == 'POST':
        form = CustomUserCreationForm()
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)
Here we enter the user details to create the new user
When you try to create the user with the same username, it will show a
message - A user with that username already exists.


We can also extend this CustomeUserCreationForm by adding more fields and
functionality and we can also use the form.ModelForm class. But in this
tutorial, we have used the form.Form class. In the upcoming tutorial,
we will implement the email verification property where user receives the
mail for verification. To create an email verification facility, we need to
store some additional data about the user, and in this tutorial we have no
way to do so. We will do this upcoming User Model tutorial.


'''