'''
1.Django Form Widget | Creating forms using various widgets:

we will learn how we can apply the various widgets in the form.
Django forms come with various attributes that enhance the appearance of the form.
There are many built-in classes, but we will cover the most commonly used form widgets.
These widgets will help to create more interactive form for any site.

2.Creating Projects:

All we start with is creating the Django project and app. Then we set the
basic configuration of the newly created app. There are three ways to create
the form in Django - Using Model Form, Using the Form class, and simple HTML
form. We will use the Form class.

3.Creating Form

Creating a forms.py file in sampleapp under the Hello project

Hello>sampleapp>forms.py

Example -

class SampleForrm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()

To render this form, we need to create the view and template that will used
to display the form to the screen.

views.py

from django.shortcuts import redirect, render
from .forms import SampleForm
def newform(request):
    form = SampleForm(request.POST or None)
    return render(request, 'sampleform.html', {'form': form})
Base.html

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Contact Us</title>
  </head>
  <body style = "background-color: #63eb8e">
  <div class = 'col-md-8'>
     {% if messages %}
        <ul>
            {% for message in messages %}
              <div class = 'alert alert-{{message.tags}}'>
                {{ message }}
              </div>
              {% endfor %}
        </ul>
    {% endif %}
  </div>
  {% block content %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    {% endblock content %}
  </body>
</html>
</textarea></div>
<p>In template/sampleform.html file -</p>
<div class="codeblock"><textarea name="code" class="xml">
{% extends 'base.html' %}
{% block content %}
<div class = "container-md" >
    <h1 class = "display-5"> Contact Us </h1>
    <hr style = "border-top: 3px double #8c8b8b">
    <form method="post" style = "margin-top: 35px; margin-bottom: 50px">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</div>
{% endblock %}

To display the form we will run the following command.

python manage.py runserver
Click on the http://127.0.0.1:8000/

4.Custom form with fields Widgets:

We create a two form-field using the CharField() field that takes in a text
We can override the default widget of each field for various uses.
The CharField() has a default widget TextInput which is the equivalent of
rendering HTML code <input type = "text">.

charField() with Teaxarea widget

We add comment field in existing form with the Textarea widget.

Example -

class SampleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)

The Textarea widget is equivalent to <textarea>....</textarea> tag, which is a multi-line text input.

CharField() with Textarea widget attributes

We can also modify the height of Textarea, specify the 'row' attribute in the widget.

Example -

class SampleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

Note - The default number of rows of Textarea is 10.

5.EmailField:

The EmailField is used to take the email input from the user. Its default input
is EmailInput and renders as <input type = "email"> in plain HTML.

This field consist of default email validator that requires a @ symbol within
the input for it to be considered valid.

Let's see the following example.

class SampleForm(forms.Form):
    email = forms.EmailField()

6.BooleanField:

As its name suggests, it takes the Boolean input from the user who is either
true or false. The default value is False and shows the unchecked checkbox in HTML form.

Example -

class SampleForm(forms.Form):
    email = forms.EmailField()
    agree = forms.BooleanField()

7.Custom Form with DataField():

The DateField() takes the value in the date format such as 2021-08-01.
The default input is DateInput but it seems like CharField.

Example -

class SampleForm(forms.Form):
    name = forms.CharField()
    date_of_birth = forms.DateField()

When we hit the submit button, it shows the "Enter a valid date" warning because
we have provides the wrong format date value.

8.DateField() with NumberInput widget attribute:

To get the number value through the dropdown, we can use the DecimalField().
The default widget is NumberInput.

Example -

from django.forms.widgets import NumberInput
class SampleForm(forms.Form):
    name = forms.CharField()
    date_of_birth = forms.DateField(widget = NumberInput(attrs={'type':'date'}))

9.DateField() with SelectDateWidget widget:

Django also provide the facility to select the date manually using the SelectDateWidget
which display three drop-down menus for month, day, and year.

Example -

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982', '1983', '1984', '1985']
lass SampleForm(forms.Form):
   name = forms.CharField()
   date_of_birth = forms.DateField(widget = SelectDateWidget(years=BIRTH_YEAR_CHOICES))

10.Custom Form with DecimalField():

To get the number value through the dropdown, we can use the DecimalField().
The default widget is NumberInput.

Example -

class SampleForm(forms.Form):
    name = forms.CharField()
    value = forms.DecimalField()

11.Custom Form with ChoiceField():

The ChoiceField() allows us to choose any one or more options from the given choices.

Example -

Choice_value = [('1', 'First'), ('2', 'Second'), ('3', 'Third')]
class SampleForm(forms.Form):
    name = forms.CharField()
    rank = forms.ChoiceField(choices=Choice_value)

12.ChoiceField() with the Select Widget:

The Select widget deals with the choices. They present the list of options to choose
from list of list of choices.

Choice_value = [('1', 'First'), ('2', 'Second'), ('3', 'Third')]
class SampleForm(forms.Form):
    name = forms.CharField()
    rank = forms.ChoiceField(widget = forms.RadioSelect, choices=Choice_value)

13.Core Arguments:

We define the core arguments which will be same for the all fields.
Below are the some important arguments.

required (Boolean)
This argument signifies that if the fields are required for form submission.
It takes a Boolean (True or false) and highlights the asterisk mark next to the field.
By default, the argument is assigned for each value is true.

Example -

class SampleForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=True)

14.max_length and min_length:

The max_length is assigned to get the maximum length of value and the min_length
is assigned to get the minimum length of value.

class SampleForm(forms.Form):
    message = forms.CharField(max_length=10)

15.Label (String):

We can create the custom label of the field using the label argument in the field.
Example -

class SampleForm(forms.Form):
    message = forms.CharField(max_length=100, label="Please write a message for us")

16.Initial (String) for CharField():

To add pre-loaded information to input, use the initial argument.

17.Initial (Boolean) for BooleanField():

We pass the initial=True to the BooleanField() to set the default clicked as the checkbox.

18.Initial (Datetime) for DateField():

We can also initiate the default value of the DatefField(). First,
we need to import datetime at the top of the file. It will set the current date.

19.MultipleChoiceField:

This field is used to show pre-define multiple choice options. User can
select the option from the predefined choices.

20.MultipleChoiceField() with CheckboxSelectMultiple widget:

We can add the multiple choice option in the form of checkbox.

21.ModelChoiceField():

Django provides the facility to use the Django model form. To do so, we need
to import the model in the forms.py file and use the ModelChoiceField() and
specify the queryset in the form field.

22.Sending Django Contact Form:

Here, we will render the Django tradition contact form. Let's see the following example.

Example -

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]
class SampleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    date_of_birth = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

Note - We use the crispy form framework and import the crispy_form_tag to the form template format files.
Example -

from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render
from .forms import SampleForm
def newform(request):
    if request.method == "POST":
        form = SampleForm(request.POST)
          if form.is_valid():
            subject = "Contact"
            body = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email'],
            'address':form.cleaned_data['address'],
            'gender':form.cleaned_data['gender'],
            'date_of_birth':form.cleaned_data['date_of_birth'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("main:homepage")
    form = SampleForm()
    return render(request, 'sampleform.html', {'form': form})

We have imported the send_mail, BadHeaderError, and HttpResponse at the top of the file.

Then, we checked the form is generated the post request and checked form is valid.
We have defined the subject and message before trying to send an email to the
specified email address in the send_mail method.

We need to require the EMAIL_BACKED in the setting.py file.

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Conclusion:

This tutorial has described the important Django forms fields and how we can
make it more user-friendly using the widget. These widgets allow us to create
more interactive forms and save from the hard coding.

'''